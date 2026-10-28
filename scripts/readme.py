#!/usr/bin/env python3
"""
Reescribe en README.md el bloque de novedades, entre sus dos marcas, a partir de updates.json.

    python3 scripts/readme.py update --readme README.md --feed updates.json
    python3 scripts/readme.py --self-test

El resto del README no se toca. Solo usa la biblioteca estándar de Python 3.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import os
import sys
import tempfile
import unittest
from pathlib import Path

import feed as feeds

START = "<!-- novedades:inicio -->"
END = "<!-- novedades:fin -->"
NOTICE = "<!-- Este bloque lo escribe .github/workflows/publish.yml con cada versión: no lo edites a mano. -->"
EMPTY_TEXT = "Todavía no hay ninguna versión publicada."


def render(feed: dict) -> str:
    """El bloque de novedades (sin las marcas): la versión actual con su descarga y las novedades de cada versión."""
    lines = [NOTICE, ""]
    android = feed.get("android")
    if android:
        asset = android["url"].rsplit("/", 1)[-1]
        lines += [
            f"**Última versión para Android: {android['versionName']}**, del {feeds.spanish_date(android['date'])} · "
            f"{feeds.android_name(android['minSdk'])} o superior · {feeds.format_size(android['size'])}",
            "",
            f"[Descargar {asset}]({android['url']}) · SHA-256 `{android['sha256']}`",
            "",
        ]
    ios = feed.get("ios")
    if isinstance(ios, dict) and isinstance(ios.get("version"), str) and feeds.VERSION_RE.fullmatch(ios["version"]) \
            and "url" in ios:
        when = f", del {feeds.spanish_date(ios['date'])}" if feeds.is_date(ios.get("date")) else ""
        lines += [f"**Última versión para iOS: {ios['version']}**{when} · [Abrir]({ios['url']})", ""]
    releases = feed.get("releases") or []
    if not releases and not android:
        lines += [EMPTY_TEXT, ""]
    for entry in releases:
        title = f"### {entry['version']} · {feeds.spanish_date(entry['date'])}"
        if entry["platforms"] != ["android"]:
            title += f" · {feeds.platform_names(entry['platforms'])}"
        lines += [title, *(f"- {feeds.escape_markdown(note)}" for note in entry["notes"]), ""]
    return "\n".join(lines).rstrip("\n") + "\n"


def replace_block(text: str, block: str) -> str:
    """[text] (el README) con [block] entre las marcas. Respeta los finales de línea que ya tenga (LF o CRLF)."""
    crlf = "\r\n" in text
    text = text.replace("\r\n", "\n")
    if text.count(START) != 1 or text.count(END) != 1 or text.index(START) > text.index(END):
        raise feeds.FeedError(f"README.md tiene que tener una vez «{START}» y, debajo, una vez «{END}»")
    before, rest = text.split(START, 1)
    after = rest.split(END, 1)[1]
    result = f"{before}{START}\n{block}{END}{after}"
    return result.replace("\n", "\r\n") if crlf else result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Reescribe el bloque de novedades de README.md.")
    parser.add_argument("--self-test", action="store_true", help="ejecuta las pruebas del script")
    commands = parser.add_subparsers(dest="command")
    update_parser = commands.add_parser("update", help="reescribe el bloque a partir del feed")
    update_parser.add_argument("--readme", type=Path, required=True)
    update_parser.add_argument("--feed", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.self_test:
        return run_self_test()
    if args.command is None:
        parser.print_help()
        return 2
    try:
        feed = feeds.check_feed(feeds.load_json(args.feed))
        with args.readme.open(encoding="utf-8", newline="") as file:
            current = file.read()
        updated = replace_block(current, render(feed))
        if updated != current:
            with args.readme.open("w", encoding="utf-8", newline="") as file:
                file.write(updated)
            print(f"{args.readme.name}: novedades reescritas.")
        else:
            print(f"{args.readme.name}: ya estaba al día.")
    except (feeds.FeedError, OSError) as error:
        feeds.report_error(str(error))
        return 1
    return 0


# ---------------------------------------------------------------------------------------------------------------------
# Pruebas (--self-test)
# ---------------------------------------------------------------------------------------------------------------------

TEMPLATE_README = Path(__file__).resolve().parent.parent / "README.md"
README = f"""# Claqueta

Texto de antes.

## Novedades

{START}
Lo que hubiera.
{END}

## Después

Texto de después.
"""
REPO = "repotoolsapps/claqueta-updates"


def published(*versions: tuple[int, str, str]) -> dict:
    """Un feed con esas versiones (versionCode, versionName, fecha) publicadas para Android, en orden."""
    current = dict(feeds.EMPTY)
    for code, name, date in versions:
        release = feeds.sample_release(code, name, date=date)
        current, _ = feeds.update(current, release, feeds.asset_url(REPO, name), f"{date}T12:00:00Z")
    return current


class ReadmeTest(unittest.TestCase):
    def test_sin_versiones_publicadas(self):
        block = render(feeds.EMPTY)
        self.assertEqual(f"{NOTICE}\n\n{EMPTY_TEXT}\n", block)

    def test_una_y_dos_versiones(self):
        block = render(published((16, "0.16.0", "2026-10-28")))
        self.assertIn("**Última versión para Android: 0.16.0**, del 28 de octubre de 2026 · Android 7.0 o superior", block)
        self.assertIn("[Descargar claqueta-0.16.0.apk](https://github.com/repotoolsapps/claqueta-updates/releases/"
                      "download/v0.16.0/claqueta-0.16.0.apk) · SHA-256 `", block)
        self.assertIn("### 0.16.0 · 28 de octubre de 2026\n- Novedad de la 0.16.0.\n", block)
        self.assertNotIn(EMPTY_TEXT, block)
        block = render(published((16, "0.16.0", "2026-10-28"), (17, "0.17.0", "2026-11-02")))
        self.assertIn("Última versión para Android: 0.17.0**, del 2 de noviembre de 2026", block)
        self.assertLess(block.index("### 0.17.0"), block.index("### 0.16.0"))

    def test_plataformas_ios_y_novedades_con_simbolos(self):
        feed = {**feeds.EMPTY,
                "ios": {"version": "1.0.0", "build": 1, "date": "2027-01-05", "url": "https://apps.apple.com/app/id1"},
                "releases": [{"version": "1.0.0", "date": "2027-01-05", "platforms": ["android", "ios"],
                              "notes": ["Ahora en <iPhone> y *iPad*."]}]}
        block = render(feeds.check_feed(feed))
        self.assertIn("**Última versión para iOS: 1.0.0**, del 5 de enero de 2027 · [Abrir](https://apps.apple.com/app/id1)",
                      block)
        self.assertIn("### 1.0.0 · 5 de enero de 2027 · Android, iOS\n- Ahora en \\<iPhone\\> y \\*iPad\\*.\n", block)
        self.assertNotIn(EMPTY_TEXT, block)

    def test_reemplaza_solo_el_bloque_e_idempotente(self):
        block = render(published((16, "0.16.0", "2026-10-28")))
        once = replace_block(README, block)
        self.assertTrue(once.startswith("# Claqueta\n\nTexto de antes.\n\n## Novedades\n\n" + START + "\n" + NOTICE))
        self.assertTrue(once.endswith(END + "\n\n## Después\n\nTexto de después.\n"))
        self.assertNotIn("Lo que hubiera.", once)
        self.assertEqual(once, replace_block(once, block))

    def test_conserva_crlf(self):
        block = render(feeds.EMPTY)
        result = replace_block(README.replace("\n", "\r\n"), block)
        self.assertNotIn("\n", result.replace("\r\n", ""))
        self.assertEqual(result, replace_block(result, block))

    def test_marcas_que_faltan_sobran_o_van_al_reves(self):
        for text in (README.replace(START, ""), README.replace(END, ""), README + START,
                     f"{END}\n{START}\n", "Sin marcas.\n"):
            with self.assertRaises(feeds.FeedError):
                replace_block(text, "x\n")

    def test_orden_update_de_punta_a_punta(self):
        with tempfile.TemporaryDirectory() as folder:
            readme, feed_file = Path(folder, "README.md"), Path(folder, "updates.json")
            readme.write_text(README, encoding="utf-8")
            feed_file.write_text(feeds.feed_text(published((16, "0.16.0", "2026-10-28"))), encoding="utf-8")
            with _quiet():
                self.assertEqual(0, main(["update", "--readme", str(readme), "--feed", str(feed_file)]))
                first = readme.read_text(encoding="utf-8")
                self.assertEqual(0, main(["update", "--readme", str(readme), "--feed", str(feed_file)]))
            self.assertEqual(first, readme.read_text(encoding="utf-8"))
            self.assertIn("### 0.16.0", first)
            feed_file.write_text('{"schema": 2}', encoding="utf-8")
            with _quiet():
                self.assertEqual(1, main(["update", "--readme", str(readme), "--feed", str(feed_file)]))

    @unittest.skipUnless(TEMPLATE_README.is_file() and feeds.TEMPLATE_FEED.is_file(), "no hay README.md y updates.json")
    def test_el_readme_del_repositorio_esta_al_dia_con_updates_json(self):
        text = TEMPLATE_README.read_text(encoding="utf-8")
        feed = feeds.check_feed(feeds.load_json(feeds.TEMPLATE_FEED))
        self.assertEqual(text, replace_block(text, render(feed)))


@contextlib.contextmanager
def _quiet():
    previous = os.environ.get("GITHUB_ACTIONS")
    os.environ["GITHUB_ACTIONS"] = "false"
    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            yield
    finally:
        if previous is None:
            os.environ.pop("GITHUB_ACTIONS", None)
        else:
            os.environ["GITHUB_ACTIONS"] = previous


def run_self_test() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ReadmeTest)
    result = unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
