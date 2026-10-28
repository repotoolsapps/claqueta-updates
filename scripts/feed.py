#!/usr/bin/env python3
"""
El feed de actualizaciones de Claqueta (updates.json) y las entregas que llegan por la rama «incoming».

    validate  Comprueba la entrega: release.json bien formado, el APK con su tamaño y su SHA-256, y un versionCode
              mayor que el del feed (o la misma entrega ya publicada, si se repite la ejecución).
    notes     Escribe el texto de la release de GitHub (Markdown).
    update    Apunta el bloque «android» del feed a la release nueva y pone sus novedades arriba en «releases».

    python3 scripts/feed.py validate --incoming ../entrega/incoming --feed updates.json --repo dueño/repo
    python3 scripts/feed.py notes --release ../entrega/incoming/release.json --repo dueño/repo --out notas.md
    python3 scripts/feed.py update --release ../entrega/incoming/release.json --feed updates.json --repo dueño/repo
    python3 scripts/feed.py --self-test

El feed (esquema 1) es lo que lee la app:

    {"schema": 1, "app": "com.repotools.claqueta", "updated": "2026-10-28T21:30:00Z",
     "android": {"versionCode", "versionName", "date", "minSdk", "url", "size", "sha256", "certSha256"} o null,
     "ios": null (reservado para cuando haya versión de iOS),
     "releases": [{"version", "date", "platforms", "notes"}, ...]}   de la más nueva a la más antigua

Quien lo lee ignora los campos que no conoce y no se fía de un esquema mayor que el suyo. Solo usa la biblioteca
estándar de Python 3.
"""
from __future__ import annotations

import argparse
import contextlib
import copy
import datetime
import hashlib
import io
import json
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path

APP_ID = "com.repotools.claqueta"
SCHEMA = 1
FEED_KEYS = ("schema", "app", "updated", "android", "ios", "releases")
VERSION_RE = re.compile(r"[0-9]+(?:\.[0-9]+)*(?:-[0-9A-Za-z]+(?:\.[0-9A-Za-z]+)*)?")
DATE_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
HEX64_RE = re.compile(r"[0-9a-f]{64}")
COMMIT_RE = re.compile(r"[0-9a-f]{40}|[0-9a-f]{64}")
REPO_RE = re.compile(r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?/[A-Za-z0-9._-]+")
# https, o http a la propia máquina (solo para probar la app en local con -PupdateFeedUrl=http://127.0.0.1:8099/...).
URL_RE = re.compile(r"(?:https://|http://(?:127\.0\.0\.1|localhost)(?::[0-9]+)?/)[^\s()<>\"'`]+")
PLATFORMS = ("android", "ios")
PLATFORM_NAMES = {"android": "Android", "ios": "iOS"}
# Android acepta versionCode hasta 2^31-1, pero Google Play se queda en 2100000000: mejor no pasarse nunca.
MAX_VERSION_CODE = 2_100_000_000
ANDROID_VERSIONS = {
    24: "7.0", 25: "7.1", 26: "8.0", 27: "8.1", 28: "9", 29: "10", 30: "11", 31: "12", 32: "12L", 33: "13",
    34: "14", 35: "15", 36: "16", 37: "17",
}
MONTHS = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
          "noviembre", "diciembre")
NEW = "nueva"
REPEATED = "repetida"


class FeedError(Exception):
    """La entrega o el feed no están como deben; el mensaje dice qué falla."""


# ---------------------------------------------------------------------------------------------------------------------
# Lectura y validación
# ---------------------------------------------------------------------------------------------------------------------


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except FileNotFoundError:
        raise FeedError(f"no existe {path}") from None
    except (ValueError, UnicodeDecodeError) as error:
        raise FeedError(f"{path.name} no es JSON válido: {error}") from None


def check_feed(feed: object) -> dict:
    """[feed] como dict, si sigue el esquema 1. Se valida entero para no publicar encima de un feed roto."""
    if not isinstance(feed, dict):
        raise FeedError("el feed no es un objeto JSON")
    schema = feed.get("schema")
    if not _is_int(schema) or schema < 1:
        raise FeedError("el feed no tiene un «schema» válido")
    if schema > SCHEMA:
        raise FeedError(f"el feed usa el esquema {schema} y estos scripts solo entienden el {SCHEMA}")
    if feed.get("app") != APP_ID:
        raise FeedError(f"el feed es de «{feed.get('app')}», no de {APP_ID}")
    if "updated" in feed and not isinstance(feed["updated"], str):
        raise FeedError("«updated» del feed tiene que ser un texto")
    android = feed.get("android")
    if android is not None:
        _check_fields("android", android, {
            "versionCode": _version_code, "versionName": _version_name, "date": is_date, "minSdk": _min_sdk,
            "url": _url, "size": _size, "sha256": _hex64, "certSha256": _hex64,
        })
    ios = feed.get("ios")
    if ios is not None:
        if not isinstance(ios, dict):
            raise FeedError("«ios» del feed tiene que ser null o un objeto")
        if "url" in ios and not _url(ios["url"]):
            raise FeedError("ios.url del feed no es una URL https")
    releases = feed.get("releases", [])
    if not isinstance(releases, list):
        raise FeedError("«releases» del feed tiene que ser una lista")
    for index, entry in enumerate(releases):
        _check_fields(f"releases[{index}]", entry, {
            "version": _version_name, "date": is_date, "platforms": _platforms, "notes": _notes_or_empty,
        })
    return feed


def check_release(release: object) -> dict:
    """[release] (release.json de la entrega) como dict, si tiene todos sus campos bien."""
    _check_fields("release.json", release, {
        "versionCode": _version_code, "versionName": _version_name, "date": is_date, "minSdk": _min_sdk,
        "size": _size, "sha256": _hex64, "certSha256": _hex64, "notes": _notes, "platforms": _platforms,
        "sourceCommit": lambda value: isinstance(value, str) and COMMIT_RE.fullmatch(value) is not None,
    })
    if "android" not in release["platforms"]:
        raise FeedError("release.json no es de Android (platforms no incluye «android»)")
    return release


def _check_fields(name: str, value: object, fields: dict) -> None:
    if not isinstance(value, dict):
        raise FeedError(f"{name} tiene que ser un objeto JSON")
    for key, valid in fields.items():
        if key not in value:
            raise FeedError(f"a {name} le falta «{key}»")
        if not valid(value[key]):
            raise FeedError(f"{name}: «{key}» no es válido ({json.dumps(value[key], ensure_ascii=False)[:80]})")


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _version_code(value: object) -> bool:
    return _is_int(value) and 1 <= value <= MAX_VERSION_CODE


def _version_name(value: object) -> bool:
    return isinstance(value, str) and VERSION_RE.fullmatch(value) is not None


def is_date(value: object) -> bool:
    """[value] es una fecha AAAA-MM-DD que existe."""
    if not isinstance(value, str) or not DATE_RE.fullmatch(value):
        return False
    try:
        datetime.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _min_sdk(value: object) -> bool:
    return _is_int(value) and 1 <= value <= 1000


def _size(value: object) -> bool:
    return _is_int(value) and value > 0


def _hex64(value: object) -> bool:
    return isinstance(value, str) and HEX64_RE.fullmatch(value) is not None


def _url(value: object) -> bool:
    return isinstance(value, str) and URL_RE.fullmatch(value) is not None


def _platforms(value: object) -> bool:
    return (isinstance(value, list) and bool(value) and all(item in PLATFORMS for item in value)
            and len(set(value)) == len(value))


def _notes_or_empty(value: object) -> bool:
    return isinstance(value, list) and all(
        isinstance(note, str) and note.strip() and "\n" not in note and "\r" not in note for note in value
    )


def _notes(value: object) -> bool:
    return _notes_or_empty(value) and bool(value)


# ---------------------------------------------------------------------------------------------------------------------
# La entrega
# ---------------------------------------------------------------------------------------------------------------------


def tag_for(version_name: str) -> str:
    return f"v{version_name}"


def asset_name(version_name: str) -> str:
    return f"claqueta-{version_name}.apk"


def asset_url(repo: str, version_name: str) -> str:
    """Dónde queda el APK: el asset de la release, con URL fija y pública."""
    if not REPO_RE.fullmatch(repo):
        raise FeedError(f"«{repo}» no es un repositorio dueño/nombre")
    return f"https://github.com/{repo}/releases/download/{tag_for(version_name)}/{asset_name(version_name)}"


def incoming_apk(folder: Path, release: dict) -> Path:
    """El APK de la entrega. La carpeta trae justo release.json y claqueta-<versionName>.apk, archivos normales."""
    expected = {"release.json", asset_name(release["versionName"])}
    if not folder.is_dir():
        raise FeedError(f"no existe la carpeta {folder}")
    found = {path.name for path in folder.iterdir()}
    if found != expected:
        raise FeedError(
            f"{folder.name}/ tiene que traer justo {', '.join(sorted(expected))}; trae {', '.join(sorted(found)) or 'nada'}"
        )
    for name in expected:
        path = folder / name
        if path.is_symlink() or not path.is_file():
            raise FeedError(f"{folder.name}/{name} no es un archivo normal")
    return folder / asset_name(release["versionName"])


def check_apk(release: dict, apk: Path) -> None:
    """El APK es exactamente el que describe release.json (tamaño y SHA-256)."""
    size = apk.stat().st_size
    if size != release["size"]:
        raise FeedError(f"{apk.name} mide {size} bytes y release.json dice {release['size']}")
    digest = sha256_file(apk)
    if digest != release["sha256"]:
        raise FeedError(f"el SHA-256 de {apk.name} es {digest} y release.json dice {release['sha256']}")


def same_android_release(android: dict | None, release: dict) -> bool:
    """[release] es justo la versión que ya publica el bloque «android» del feed."""
    return android is not None and (
        android["versionCode"], android["versionName"], android["sha256"]
    ) == (release["versionCode"], release["versionName"], release["sha256"])


def classify(feed: dict, release: dict) -> str:
    """
    NEW si [release] se puede publicar encima de [feed]; REPEATED si es justo lo que ya está publicado (una ejecución
    repetida, que no cambia nada). Cualquier otra cosa (versionCode que no sube, el mismo con otro APK, un versionName
    que ya salió para Android) es un error.
    """
    android = feed.get("android")
    if same_android_release(android, release):
        return REPEATED
    if android is not None and release["versionCode"] <= android["versionCode"]:
        raise FeedError(
            f"versionCode {release['versionCode']} ({release['versionName']}) no es mayor que el publicado "
            f"({android['versionCode']}, {android['versionName']})"
        )
    published = {entry["version"] for entry in feed.get("releases", []) if "android" in entry["platforms"]}
    if android is not None:
        published.add(android["versionName"])
    if release["versionName"] in published:
        raise FeedError(f"la versión {release['versionName']} ya se publicó para Android con otro versionCode")
    return NEW


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for block in iter(lambda: file.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


# ---------------------------------------------------------------------------------------------------------------------
# El feed nuevo
# ---------------------------------------------------------------------------------------------------------------------


def android_block(release: dict, url: str) -> dict:
    return {
        "versionCode": release["versionCode"],
        "versionName": release["versionName"],
        "date": release["date"],
        "minSdk": release["minSdk"],
        "url": url,
        "size": release["size"],
        "sha256": release["sha256"],
        "certSha256": release["certSha256"],
    }


def update(feed: dict, release: dict, url: str, now: str) -> tuple[dict, bool]:
    """
    El feed con [release] publicada y si ha cambiado algo. «android» pasa a la versión nueva; en «releases» entra su
    entrada arriba (si esa versión ya había salido para otra plataforma, se juntan en una), sin duplicados y de la más
    nueva a la más antigua. «updated» solo se toca si cambia algo, así que repetir la misma entrega no cambia nada.
    """
    repeated = classify(feed, release) == REPEATED
    new = copy.deepcopy(feed)
    if not repeated:
        new["android"] = android_block(release, url)
    entry = {
        "version": release["versionName"],
        "date": release["date"],
        "platforms": _ordered(release["platforms"]),
        "notes": list(release["notes"]),
    }
    releases: list[dict] = []
    seen: set[str] = set()
    for item in new.get("releases", []):
        if item["version"] in seen:
            continue
        seen.add(item["version"])
        if item["version"] == entry["version"] and not repeated:
            item = {
                **item,
                "date": min(item["date"], entry["date"]),
                "platforms": _ordered([*item["platforms"], *entry["platforms"]]),
                "notes": entry["notes"],
            }
        releases.append(item)
    if entry["version"] not in seen:
        releases.insert(0, entry)
    # sorted() es estable: con la misma fecha, la entrada nueva (insertada la primera) sigue arriba.
    new["releases"] = sorted(releases, key=lambda item: item["date"], reverse=True)
    changed = new != feed
    if changed:
        new["updated"] = now
    return canonical(new), changed


def canonical(feed: dict) -> dict:
    """[feed] con las claves en el orden del contrato y las desconocidas detrás, tal cual."""
    ordered = {key: feed[key] for key in FEED_KEYS if key in feed}
    ordered.update((key, value) for key, value in feed.items() if key not in ordered)
    return ordered


def feed_text(feed: dict) -> str:
    return json.dumps(canonical(feed), ensure_ascii=False, indent=2) + "\n"


def utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _ordered(platforms: list[str]) -> list[str]:
    return [platform for platform in PLATFORMS if platform in platforms]


# ---------------------------------------------------------------------------------------------------------------------
# Textos (también los usa readme.py)
# ---------------------------------------------------------------------------------------------------------------------


def format_size(size: int) -> str:
    """Tamaño como lo cuenta Android (1 MB = 1 000 000 bytes), con coma decimal: «40,6 MB»."""
    if size < 1_000_000:
        return f"{max(1, round(size / 1000))} kB"
    return f"{size / 1_000_000:.1f}".replace(".", ",") + " MB"


def android_name(min_sdk: int) -> str:
    """«Android 7.0» para la API 24."""
    version = ANDROID_VERSIONS.get(min_sdk)
    return f"Android {version}" if version else f"Android (API {min_sdk})"


def spanish_date(date: str) -> str:
    """«28 de octubre de 2026» para 2026-10-28."""
    day = datetime.date.fromisoformat(date)
    return f"{day.day} de {MONTHS[day.month - 1]} de {day.year}"


def platform_names(platforms: list[str]) -> str:
    return ", ".join(PLATFORM_NAMES.get(platform, platform) for platform in platforms)


def escape_markdown(text: str) -> str:
    """Una novedad (texto plano) lista para meterla en Markdown sin que nada se interprete como formato."""
    escaped = re.sub(r"([\\`*_\[\]<>~|#])", r"\\\1", text)
    return re.sub(r"^([0-9]+)([.)])|^([+-])", lambda m: f"{m.group(1)}\\{m.group(2)}" if m.group(1) else f"\\{m.group(3)}",
                  escaped)


def release_notes(release: dict, repo: str) -> str:
    """El texto de la release de GitHub: novedades, requisitos y cómo comprobar la descarga."""
    name = asset_name(release["versionName"])
    lines = [
        *(f"- {escape_markdown(note)}" for note in release["notes"]),
        "",
        f"**{android_name(release['minSdk'])} o superior** · `{name}` · {format_size(release['size'])}",
        "",
        f"¿Primera vez? Descarga `{name}` aquí abajo, en Assets, y sigue "
        f"[estos pasos](https://github.com/{repo}#instalar-claqueta-por-primera-vez). Después, Claqueta se "
        "actualiza sola.",
        "",
        f"SHA-256 del APK: `{release['sha256']}`",
        "",
        f"SHA-256 del certificado de firma: `{release['certSha256']}`",
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------------------------------------------------
# Línea de comandos
# ---------------------------------------------------------------------------------------------------------------------


def write_outputs(values: dict[str, str]) -> None:
    """Deja [values] para los pasos siguientes ($GITHUB_OUTPUT) y en el registro."""
    lines = []
    for key, value in values.items():
        if "\n" in value or "\r" in value:
            raise ValueError(f"{key} no puede tener saltos de línea")
        lines.append(f"{key}={value}\n")
    sys.stdout.writelines(lines)
    target = os.environ.get("GITHUB_OUTPUT")
    if target:
        with open(target, "a", encoding="utf-8") as file:
            file.writelines(lines)


def report_error(message: str) -> None:
    """Cuenta el error; dentro de GitHub Actions, como anotación."""
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print("::error::" + message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A"), flush=True)
    else:
        print(f"error: {message}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="El feed de actualizaciones de Claqueta y sus entregas.")
    parser.add_argument("--self-test", action="store_true", help="ejecuta las pruebas del script")
    commands = parser.add_subparsers(dest="command")

    validate_parser = commands.add_parser("validate", help="comprueba la entrega de incoming/")
    validate_parser.add_argument("--incoming", type=Path, required=True, help="la carpeta incoming/ de la entrega")
    validate_parser.add_argument("--feed", type=Path, required=True)
    validate_parser.add_argument("--repo", required=True, help="dueño/nombre del repositorio público")

    notes_parser = commands.add_parser("notes", help="escribe el texto de la release de GitHub")
    notes_parser.add_argument("--release", type=Path, required=True)
    notes_parser.add_argument("--repo", required=True)
    notes_parser.add_argument("--out", type=Path, required=True)

    update_parser = commands.add_parser("update", help="publica la entrega en el feed")
    update_parser.add_argument("--release", type=Path, required=True)
    update_parser.add_argument("--feed", type=Path, required=True)
    update_parser.add_argument("--repo", required=True)
    update_parser.add_argument("--now", help="AAAA-MM-DDTHH:MM:SSZ (por defecto, ahora en UTC)")
    update_parser.add_argument("--url", help="URL del APK en vez del asset de la release (pruebas en local)")

    args = parser.parse_args(argv)
    if args.self_test:
        return run_self_test()
    if args.command is None:
        parser.print_help()
        return 2
    try:
        if args.command == "validate":
            release = check_release(load_json(args.incoming / "release.json"))
            feed = check_feed(load_json(args.feed))
            apk = incoming_apk(args.incoming, release)
            check_apk(release, apk)
            mode = classify(feed, release)
            url = asset_url(args.repo, release["versionName"])
            published = feed.get("android")
            print(
                f"Entrega {mode}: {release['versionName']} (versionCode {release['versionCode']}), "
                f"{format_size(release['size'])}, SHA-256 {release['sha256']}; en el feed: "
                + (f"{published['versionName']} (versionCode {published['versionCode']})." if published else "nada.")
            )
            write_outputs({
                "mode": mode,
                "version_name": release["versionName"],
                "version_code": str(release["versionCode"]),
                "tag": tag_for(release["versionName"]),
                "asset_name": apk.name,
                "asset_url": url,
                "sha256": release["sha256"],
                "size": str(release["size"]),
            })
        elif args.command == "notes":
            release = check_release(load_json(args.release))
            asset_url(args.repo, release["versionName"])
            args.out.write_text(release_notes(release, args.repo), encoding="utf-8")
            print(f"Notas de {tag_for(release['versionName'])} en {args.out}.")
        else:
            release = check_release(load_json(args.release))
            feed = check_feed(load_json(args.feed))
            url = args.url or asset_url(args.repo, release["versionName"])
            if not _url(url):
                raise FeedError(f"«{url}» no es una URL https (ni http a 127.0.0.1 o localhost, para pruebas)")
            new, changed = update(feed, release, url, args.now or utc_now())
            check_feed(new)
            text = feed_text(new)
            if text != args.feed.read_text(encoding="utf-8"):
                args.feed.write_text(text, encoding="utf-8")
            print(f"{args.feed.name}: " + ("publicada " + release["versionName"] if changed else "sin cambios") + ".")
            write_outputs({"changed": "true" if changed else "false"})
    except (FeedError, OSError) as error:
        report_error(str(error))
        return 1
    return 0


# ---------------------------------------------------------------------------------------------------------------------
# Pruebas (--self-test)
# ---------------------------------------------------------------------------------------------------------------------

REPO = "repotoolsapps/claqueta-updates"
TEMPLATE_FEED = Path(__file__).resolve().parent.parent / "updates.json"
EMPTY = {"schema": 1, "app": APP_ID, "updated": "2026-10-28T20:00:00Z", "android": None, "ios": None, "releases": []}


def sample_release(code: int, name: str, apk: bytes = b"", date: str = "2026-10-28", notes=None) -> dict:
    data = apk or f"APK {name}".encode()
    return {
        "versionCode": code, "versionName": name, "date": date, "minSdk": 24, "size": len(data),
        "sha256": hashlib.sha256(data).hexdigest(), "certSha256": "c" * 64,
        "notes": notes or [f"Novedad de la {name}."], "platforms": ["android"], "sourceCommit": "a" * 40,
    }


class FeedTest(unittest.TestCase):
    def assert_feed_error(self, fragment: str, function, *args):
        with self.assertRaises(FeedError) as caught:
            function(*args)
        self.assertIn(fragment, str(caught.exception))

    def test_primera_entrega_con_el_feed_vacio(self):
        release = sample_release(16, "0.16.0")
        self.assertEqual(NEW, classify(EMPTY, release))
        feed, changed = update(EMPTY, release, asset_url(REPO, "0.16.0"), "2026-10-28T21:30:00Z")
        self.assertTrue(changed)
        self.assertEqual("2026-10-28T21:30:00Z", feed["updated"])
        self.assertEqual(
            "https://github.com/repotoolsapps/claqueta-updates/releases/download/v0.16.0/claqueta-0.16.0.apk",
            feed["android"]["url"],
        )
        self.assertEqual(["versionCode", "versionName", "date", "minSdk", "url", "size", "sha256", "certSha256"],
                         list(feed["android"]))
        self.assertEqual([{"version": "0.16.0", "date": "2026-10-28", "platforms": ["android"],
                           "notes": ["Novedad de la 0.16.0."]}], feed["releases"])
        self.assertEqual(list(FEED_KEYS), list(feed))
        self.assertIsNone(feed["ios"])
        check_feed(feed)

    def test_segunda_entrega_va_arriba(self):
        first, _ = update(EMPTY, sample_release(16, "0.16.0"), asset_url(REPO, "0.16.0"), "2026-10-28T21:30:00Z")
        release = sample_release(17, "0.17.0", date="2026-11-02")
        self.assertEqual(NEW, classify(first, release))
        second, changed = update(first, release, asset_url(REPO, "0.17.0"), "2026-11-02T08:00:00Z")
        self.assertTrue(changed)
        self.assertEqual(17, second["android"]["versionCode"])
        self.assertEqual(["0.17.0", "0.16.0"], [entry["version"] for entry in second["releases"]])
        self.assertEqual(16, first["android"]["versionCode"], "update no toca el feed que recibe")

    def test_repetir_la_misma_entrega_no_cambia_nada(self):
        release = sample_release(16, "0.16.0")
        feed, _ = update(EMPTY, release, asset_url(REPO, "0.16.0"), "2026-10-28T21:30:00Z")
        self.assertEqual(REPEATED, classify(feed, release))
        again, changed = update(feed, release, asset_url(REPO, "0.16.0"), "2026-10-29T09:00:00Z")
        self.assertFalse(changed)
        self.assertEqual(feed_text(feed), feed_text(again))
        # Aunque la entrega repetida traiga otra fecha (otro release.json), lo publicado se queda como estaba.
        later, changed = update(feed, {**release, "date": "2026-10-29"}, asset_url(REPO, "0.16.0"), "x")
        self.assertFalse(changed)
        self.assertEqual("2026-10-28", later["android"]["date"])

    def test_mismo_versioncode_con_otro_apk_o_versioncode_menor(self):
        feed, _ = update(EMPTY, sample_release(16, "0.16.0"), asset_url(REPO, "0.16.0"), "2026-10-28T21:30:00Z")
        self.assert_feed_error("no es mayor que el publicado", classify, feed, sample_release(16, "0.16.0", b"otro"))
        self.assert_feed_error("no es mayor que el publicado", classify, feed, sample_release(15, "0.15.9"))
        self.assert_feed_error("no es mayor que el publicado", update, feed, sample_release(15, "0.15.9"), "u", "n")

    def test_versionname_ya_publicado_con_otro_versioncode(self):
        feed, _ = update(EMPTY, sample_release(16, "0.16.0"), asset_url(REPO, "0.16.0"), "2026-10-28T21:30:00Z")
        self.assert_feed_error("ya se publicó para Android", classify, feed, sample_release(17, "0.16.0"))

    def test_misma_version_publicada_antes_en_ios_se_junta(self):
        feed = {**EMPTY, "ios": {"version": "0.16.0", "build": 3, "date": "2026-10-20",
                                 "url": "https://testflight.apple.com/join/abc"},
                "releases": [{"version": "0.16.0", "date": "2026-10-20", "platforms": ["ios"], "notes": ["iPhone."]}]}
        new, changed = update(check_feed(feed), sample_release(16, "0.16.0"), asset_url(REPO, "0.16.0"), "n")
        self.assertTrue(changed)
        self.assertEqual([{"version": "0.16.0", "date": "2026-10-20", "platforms": ["android", "ios"],
                           "notes": ["Novedad de la 0.16.0."]}], new["releases"])
        self.assertEqual(feed["ios"], new["ios"])

    def test_conserva_campos_desconocidos_y_quita_duplicados(self):
        feed = {**EMPTY, "mirror": "https://example.org/updates.json", "releases": [
            {"version": "0.15.0", "date": "2026-10-20", "platforms": ["android"], "notes": ["A."], "extra": 1},
            {"version": "0.14.0", "date": "2026-10-25", "platforms": ["android"], "notes": ["B."]},
            {"version": "0.15.0", "date": "2026-10-19", "platforms": ["android"], "notes": ["Duplicada."]},
        ]}
        feed["android"] = android_block(sample_release(15, "0.15.0"), asset_url(REPO, "0.15.0"))
        new, _ = update(check_feed(feed), sample_release(16, "0.16.0"), asset_url(REPO, "0.16.0"), "n")
        self.assertEqual(["0.16.0", "0.14.0", "0.15.0"], [entry["version"] for entry in new["releases"]])
        self.assertEqual(1, new["releases"][2]["extra"])
        self.assertEqual("https://example.org/updates.json", new["mirror"])
        self.assertEqual("mirror", list(new)[-1])

    def test_misma_fecha_la_nueva_arriba(self):
        feed = {**EMPTY, "releases": [{"version": "0.15.0", "date": "2026-10-28", "platforms": ["android"],
                                       "notes": ["A."]}]}
        new, _ = update(feed, sample_release(16, "0.16.0"), asset_url(REPO, "0.16.0"), "n")
        self.assertEqual(["0.16.0", "0.15.0"], [entry["version"] for entry in new["releases"]])

    def test_release_json_mal_formado(self):
        good = sample_release(16, "0.16.0")
        check_release(good)
        for change, fragment in (
            ({"versionCode": "16"}, "versionCode"),
            ({"versionCode": True}, "versionCode"),
            ({"versionCode": 0}, "versionCode"),
            ({"versionName": "v0.16.0"}, "versionName"),
            ({"date": "2026-13-01"}, "date"),
            ({"sha256": "A" * 64}, "sha256"),
            ({"certSha256": "c" * 63}, "certSha256"),
            ({"notes": []}, "notes"),
            ({"notes": ["Dos\nlíneas"]}, "notes"),
            ({"notes": ["  "]}, "notes"),
            ({"platforms": ["ios"]}, "no es de Android"),
            ({"platforms": ["android", "android"]}, "platforms"),
            ({"platforms": ["windows"]}, "platforms"),
            ({"size": 0}, "size"),
            ({"sourceCommit": "main"}, "sourceCommit"),
        ):
            self.assert_feed_error(fragment, check_release, {**good, **change})
        incomplete = dict(good)
        del incomplete["minSdk"]
        self.assert_feed_error("le falta «minSdk»", check_release, incomplete)
        self.assert_feed_error("objeto", check_release, [good])

    def test_feed_con_esquema_2_otra_app_o_roto(self):
        for change, fragment in (
            ({"schema": 2}, "esquema 2"),
            ({"schema": 0}, "schema"),
            ({"app": "com.otra"}, "com.otra"),
            ({"android": {"versionCode": 1}}, "le falta"),
            ({"releases": [{"version": "1.0"}]}, "le falta"),
            ({"releases": {}}, "lista"),
            ({"ios": "1.0"}, "ios"),
            ({"ios": {"url": "http://inseguro"}}, "ios.url"),
            ({"updated": 5}, "updated"),
        ):
            self.assert_feed_error(fragment, check_feed, {**EMPTY, **change})

    def test_apk_y_carpeta_de_la_entrega(self):
        with tempfile.TemporaryDirectory() as folder:
            incoming = Path(folder, "incoming")
            incoming.mkdir()
            data = os.urandom(3000)
            release = sample_release(16, "0.16.0", data)
            (incoming / "release.json").write_text(json.dumps(release), encoding="utf-8")
            (incoming / "claqueta-0.16.0.apk").write_bytes(data)
            apk = incoming_apk(incoming, release)
            check_apk(release, apk)
            self.assert_feed_error("mide", check_apk, {**release, "size": 2999}, apk)
            self.assert_feed_error("SHA-256", check_apk, {**release, "sha256": "0" * 64}, apk)
            (incoming / "otro.txt").write_text("sobra")
            self.assert_feed_error("tiene que traer justo", incoming_apk, incoming, release)
            (incoming / "otro.txt").unlink()
            (incoming / "claqueta-0.16.0.apk").rename(incoming / "claqueta.apk")
            self.assert_feed_error("tiene que traer justo", incoming_apk, incoming, release)
            (incoming / "claqueta.apk").unlink()
            (incoming / "claqueta-0.16.0.apk").symlink_to(Path(folder, "fuera.apk"))
            self.assert_feed_error("archivo normal", incoming_apk, incoming, release)
            self.assert_feed_error("no existe la carpeta", incoming_apk, Path(folder, "nada"), release)

    def test_url_del_asset_y_repositorio(self):
        self.assertEqual("https://github.com/a/b/releases/download/v1.0/claqueta-1.0.apk", asset_url("a/b", "1.0"))
        for repo in ("a", "a/b/c", "a/b c", "../x"):
            self.assert_feed_error("dueño/nombre", asset_url, repo, "1.0")
        self.assertTrue(_url("http://127.0.0.1:8099/claqueta-0.16.0.apk"))
        self.assertTrue(_url("http://localhost/claqueta.apk"))
        for url in ("http://example.com/claqueta.apk", "http://127.0.0.1.example.com/x", "https://x/a b", "ftp://x/y"):
            self.assertFalse(_url(url), url)

    def test_update_con_url_local_para_pruebas(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "updates.json").write_text(feed_text(EMPTY), encoding="utf-8")
            (root / "release.json").write_text(json.dumps(sample_release(16, "0.16.0")), encoding="utf-8")
            arguments = ["update", "--release", str(root / "release.json"), "--feed", str(root / "updates.json"),
                         "--repo", REPO, "--url"]
            with _environment(GITHUB_ACTIONS="false"), contextlib.redirect_stdout(io.StringIO()), \
                    contextlib.redirect_stderr(io.StringIO()) as errors:
                self.assertEqual(1, main(arguments + ["http://example.com/claqueta-0.16.0.apk"]))
                self.assertEqual(0, main(arguments + ["http://127.0.0.1:8099/claqueta-0.16.0.apk"]))
            self.assertIn("no es una URL https", errors.getvalue())
            feed = check_feed(load_json(root / "updates.json"))
            self.assertEqual("http://127.0.0.1:8099/claqueta-0.16.0.apk", feed["android"]["url"])

    def test_notas_de_la_release_y_textos(self):
        release = sample_release(16, "0.16.0", b"x" * 40634791,
                                 notes=["Ajustes › Acerca de", "Usa *dos* filtros_nuevos", "1. Primero", "- guion"])
        notes = release_notes(release, REPO)
        self.assertIn("- Ajustes › Acerca de\n", notes)
        self.assertIn("- Usa \\*dos\\* filtros\\_nuevos\n", notes)
        self.assertIn("- 1\\. Primero\n", notes)
        self.assertIn("- \\- guion\n", notes)
        self.assertIn("**Android 7.0 o superior** · `claqueta-0.16.0.apk` · 40,6 MB", notes)
        self.assertIn("https://github.com/repotoolsapps/claqueta-updates#instalar-claqueta-por-primera-vez", notes)
        self.assertIn(f"SHA-256 del APK: `{release['sha256']}`", notes)
        self.assertEqual("28 de octubre de 2026", spanish_date("2026-10-28"))
        self.assertEqual("1 de enero de 2027", spanish_date("2027-01-01"))
        self.assertEqual("Android (API 99)", android_name(99))
        self.assertEqual("9 kB", format_size(8538))

    def test_ordenes_de_punta_a_punta(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "updates.json").write_text(feed_text(EMPTY), encoding="utf-8")
            outputs = root / "github_output"
            plain = {"GITHUB_OUTPUT": str(outputs), "GITHUB_ACTIONS": "false"}
            for code, name in ((16, "0.16.0"), (17, "0.17.0"), (17, "0.17.0")):
                incoming = root / f"entrega-{code}" / "incoming"
                incoming.mkdir(parents=True, exist_ok=True)
                data = f"APK {name}".encode() * 100
                release = sample_release(code, name, data)
                (incoming / "release.json").write_text(json.dumps(release, indent=2).replace("\n", "\r\n"),
                                                       encoding="utf-8")
                (incoming / asset_name(name)).write_bytes(data)
                with _environment(**plain), contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(0, main(["validate", "--incoming", str(incoming), "--feed",
                                              str(root / "updates.json"), "--repo", REPO]))
                    self.assertEqual(0, main(["notes", "--release", str(incoming / "release.json"), "--repo", REPO,
                                              "--out", str(root / "notas.md")]))
                    self.assertEqual(0, main(["update", "--release", str(incoming / "release.json"), "--feed",
                                              str(root / "updates.json"), "--repo", REPO, "--now",
                                              f"2026-10-28T2{code - 16}:00:00Z"]))
            feed = check_feed(load_json(root / "updates.json"))
            self.assertEqual(17, feed["android"]["versionCode"])
            self.assertEqual("2026-10-28T21:00:00Z", feed["updated"], "la tercera (repetida) no cambia updated")
            self.assertEqual(["0.17.0", "0.16.0"], [entry["version"] for entry in feed["releases"]])
            written = outputs.read_text(encoding="utf-8")
            self.assertEqual(2, written.count("mode=nueva\n"))
            self.assertEqual(1, written.count("mode=repetida\n"))
            self.assertEqual(["changed=true", "changed=true", "changed=false"],
                             [line for line in written.splitlines() if line.startswith("changed=")])
            # Una entrega vieja se rechaza con un mensaje y código 1.
            old = root / "entrega-16" / "incoming"
            with _environment(**plain), contextlib.redirect_stderr(io.StringIO()) as errors, \
                    contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(1, main(["validate", "--incoming", str(old), "--feed", str(root / "updates.json"),
                                          "--repo", REPO]))
            self.assertIn("no es mayor que el publicado (17, 0.17.0)", errors.getvalue())

    @unittest.skipUnless(TEMPLATE_FEED.is_file(), "no hay updates.json junto a scripts/")
    def test_el_updates_json_del_repositorio_es_valido(self):
        feed = check_feed(load_json(TEMPLATE_FEED))
        self.assertEqual(feed_text(feed), TEMPLATE_FEED.read_text(encoding="utf-8"), "formato canónico")


@contextlib.contextmanager
def _environment(**values: str):
    previous = {key: os.environ.get(key) for key in values}
    os.environ.update(values)
    try:
        yield
    finally:
        for key, value in previous.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


def run_self_test() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(FeedTest)
    result = unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
