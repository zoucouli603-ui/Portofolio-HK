# HK Production — Portfolio (site statique)

Portfolio de Hamed Keita : HTML + Tailwind CSS (CDN) + Alpine.js. Aucun serveur requis.

## Structure

```
site/                  ← le site à déployer
├── index.html         page d'accueil (filtres, tarifs, contacts, modale « Demander un devis »)
├── projet/N.html      une page par réalisation
├── css/style.css      styles personnalisés (badge 3D, animations)
└── static/images/     images et vidéos
vercel.json            configuration Vercel (dossier publié : site/)
build_static.py        régénère site/ depuis data.py et les templates Flask
data.py, templates/, portfolio/   sources Flask d'origine (non déployées)
```

## Tester en local (sans Flask)

- **VS Code** : installer l'extension *Live Server*, clic droit sur `site/index.html` → *Open with Live Server*.
- **Terminal** : `npx serve site` (ou `python -m http.server 5000 -d site`), puis ouvrir l'adresse affichée.

> Une connexion Internet est nécessaire (Tailwind, Alpine.js et la police Inter sont chargés par CDN).

## Modifier le contenu

Les projets et tarifs sont dans `data.py` et `portfolio/main.py`. Après modification :

```bash
python build_static.py
```

Les images/vidéos se déposent dans `static/images/` ; le script copie dans `site/` uniquement celles utilisées.

## Déployer sur Vercel

1. Pousser le dépôt sur GitHub :
   ```bash
   git init
   git add .
   git commit -m "Site statique HK Production"
   git branch -M main
   git remote add origin https://github.com/<utilisateur>/<depot>.git
   git push -u origin main
   ```
   (le `.gitignore` fourni exclut déjà `venv/` et `instance/`)
2. Sur [vercel.com](https://vercel.com) : **Add New… → Project**, importer le dépôt.
3. Laisser le preset *Other* : `vercel.json` indique déjà de publier `site/`, sans build ni installation.
4. Cliquer sur **Deploy**. Chaque `git push` redéploie le site.

## Devis WhatsApp

Le formulaire « Demander un devis » ouvre `https://wa.me/22374016702` avec le message pré-rempli (nom, prestation, description, budget).
