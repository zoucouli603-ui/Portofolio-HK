"""Pages publiques : accueil et détail d'une réalisation du portfolio."""
from flask import Blueprint, abort, render_template, url_for

from data import PROJETS

bp = Blueprint("main", __name__)

# Informations publiques de la marque, injectées dans tous les templates
PROFIL = {
    "nom": "Hamed Keita",
    "marque": "HK Production",
    "metiers": "Graphiste, Photographe & Monteur Vidéo",
    "stats": [
        ("5+", "Ans d'expérience"),
        ("500+", "Projets réalisés"),
        ("98%", "Clients satisfaits"),
        ("100%", "Sur mesure"),
    ],
    # Icône : sigle coloré (fond / texte) ou, à défaut, SVG dédié dans index.html
    "outils": [
        {"nom": "Photoshop", "sigle": "Ps", "fond": "#001E36", "texte": "#31A8FF"},
        {"nom": "Illustrator", "sigle": "Ai", "fond": "#330000", "texte": "#FF9A00"},
        {"nom": "After Effects", "sigle": "Ae", "fond": "#00005B", "texte": "#9999FF"},
        {"nom": "Lightroom", "sigle": "Lr", "fond": "#001E36", "texte": "#31A8FF"},
        {"nom": "DaVinci Resolve", "svg": "davinci"},
        {"nom": "CapCut", "svg": "capcut"},
    ],
    "telephone": "+223 74 01 67 02",
    "telephone_href": "+22374016702",
    "email": "hkeita312@gmail.com",
    "tiktok": "@thebig_hk5",
    "tiktok_url": "https://www.tiktok.com/@thebig_hk5",
    "snapchat": "HK Production",
}


@bp.app_context_processor
def inject_profil():
    return {"profil": PROFIL}


@bp.app_template_filter("image_url")
def image_url(chemin: str) -> str:
    """URL absolue telle quelle, sinon chemin relatif au dossier static/."""
    if chemin.startswith(("http://", "https://")):
        return chemin
    return url_for("static", filename=chemin)


# Grilles tarifaires (FCFA) : (prestation, prix)
TARIFS_DESIGN = [
    ("Affiche / Flyer", "5 000 FCFA"),
    ("Carte de visite", "5 000 FCFA"),
    ("Étiquette", "5 000 FCFA"),
    ("Sticker", "3 000 FCFA"),
    ("Menu", "5 000 FCFA"),
    ("Kakemono", "15 000 FCFA"),
    ("Brochure", "10 000 FCFA"),
    ("Logo", "20 000 FCFA"),
    ("Filtre snap", "15 000 FCFA"),
]
TARIFS_PHOTO = [
    ("Photoshooting", "À partir de 15 000 FCFA"),
    ("Photos de soutenance", "À partir de 15 000 FCFA"),
    ("Photos de mariage", "100 000 à 150 000 FCFA"),
    ("Shooting professionnel", "Sur devis"),
]
TARIFS_VIDEO = [
    ("Vidéo Short (format court)", "15 000 FCFA"),
    ("Vidéo professionnelle", "À partir de 20 000 FCFA"),
    ("Vidéo publicitaire", "À partir de 20 000 FCFA"),
    ("Couverture vidéo d'événement", "Sur devis"),
    ("Vidéo promotionnelle", "Sur devis"),
]


@bp.route("/")
def index():
    return render_template(
        "index.html",
        projets=PROJETS,
        tarifs_design=TARIFS_DESIGN,
        tarifs_photo=TARIFS_PHOTO,
        tarifs_video=TARIFS_VIDEO,
    )


@bp.route("/project/<int:id>")
def project(id):
    projet = next((p for p in PROJETS if p["id"] == id), None)
    if projet is None:
        abort(404)
    return render_template("project.html", projet=projet)
