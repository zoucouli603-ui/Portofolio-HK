"""Génère le site 100 % statique dans `site/` à partir des templates Flask et de data.py.

Usage : python build_static.py
"""
import re
import shutil
from html import unescape
from pathlib import Path
from urllib.parse import unquote

from app import app
from data import PROJETS

ROOT = Path(__file__).parent
SORTIE = ROOT / "site"


def adapter(html: str, profondeur: int) -> str:
    """Convertit les URLs Flask absolues en chemins relatifs (profondeur 0 = site/, 1 = site/projet/)."""
    racine = "./" if profondeur == 0 else "../"
    html = html.replace('"/static/', f'"{racine}static/').replace("url(/static/", f"url({racine}static/")
    html = re.sub(
        r'href="/project/(\d+)"',
        lambda m: f'href="{"projet/" if profondeur == 0 else ""}{m.group(1)}.html"',
        html,
    )
    accueil = "" if profondeur == 0 else "../index.html"
    html = re.sub(r'href="/#(\w+)"', lambda m: f'href="{accueil}#{m.group(1)}"', html)
    html = html.replace('href="/"', f'href="{accueil or "#"}"' if profondeur else 'href="#"')
    return html


def extraire_css(html: str, profondeur: int) -> tuple[str, str]:
    """Sort le bloc <style> sans type vers css/style.css (le bloc Tailwind @apply reste inline)."""
    m = re.search(r"<style>(.*?)</style>", html, re.S)
    if not m:
        return html, ""
    racine = "./" if profondeur == 0 else "../"
    lien = f'<link rel="stylesheet" href="{racine}css/style.css">'
    return html[: m.start()] + lien + html[m.end():], m.group(1)


def main():
    if SORTIE.exists():
        shutil.rmtree(SORTIE)
    (SORTIE / "projet").mkdir(parents=True)
    (SORTIE / "css").mkdir()

    client = app.test_client()
    pages = {SORTIE / "index.html": ("/", 0)}
    for p in PROJETS:
        pages[SORTIE / "projet" / f"{p['id']}.html"] = (f"/project/{p['id']}", 1)

    css, fichiers = "", set()
    for chemin, (url, profondeur) in pages.items():
        rep = client.get(url)
        assert rep.status_code == 200, f"{url} -> {rep.status_code}"
        html, bloc = extraire_css(adapter(rep.get_data(as_text=True), profondeur), profondeur)
        css = css or bloc
        chemin.write_text(html, encoding="utf-8")
        fichiers.update(unquote(f) for f in re.findall(r"static/([^\")\s#<]+)", unescape(html)))

    (SORTIE / "css" / "style.css").write_text(css.strip() + "\n", encoding="utf-8")
    for f in sorted(fichiers):
        src = ROOT / "static" / f
        if not src.is_file():
            raise FileNotFoundError(src)
        dest = SORTIE / "static" / f
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dest)
    print(f"{len(pages)} pages, {len(fichiers)} fichiers statiques -> {SORTIE}")


if __name__ == "__main__":
    main()
