"""Données du portfolio de Hamed Keita (HK Production).

`image` : URL complète, ou chemin relatif à static/ (ex. "images/full-black.jpg").
`affiche` : True pour une image verticale à afficher en entier, sans recadrage.
"""

PROJETS = [
    {
        "id": 1,
        "titre": "Affiche Dîner de Promo",
        "categorie": "Design Graphique",
        "image": "images/diner-promo.jpg",
        "affiche": True,
        "description_courte": "Conception visuelle élégante pour l'événement « Dîner de Promo » (PSN1 Présente) à l'Espace loisirs Koulouba.",
        "description_longue": (
            "Conception visuelle élégante pour l'événement « Dîner de Promo » (PSN1 Présente) "
            "à l'Espace loisirs Koulouba : rideau bleu nuit, cordon doré et typographie dorée "
            "pour une ambiance de gala, avec le programme, la date, le lieu, le parrain et le PCO."
        ),
    },
    {
        "id": 2,
        "titre": "Formation Pratique en Audio-Visuel",
        "categorie": "Design Graphique",
        "image": "images/formation-audiovisuel.jpg",
        "affiche": True,
        "description_courte": "Affiche publicitaire pour la formation pratique en montage, photographie et retouche photo (Magashop).",
        "description_longue": (
            "Affiche publicitaire pour la formation pratique en audio-visuel organisée par Magashop : "
            "photographie, retouche photo, vidéo et montage. Un fond bleu vif, les icônes des logiciels "
            "enseignés, et les informations clés (tarifs, dates, rythme de la formation, contacts) "
            "mises en avant dans des blocs lisibles."
        ),
    },
    {
        "id": 3,
        "titre": "Affiche Événement « Full Black »",
        "categorie": "Design Graphique",
        "image": "images/full-black.jpg",
        "affiche": True,
        "description_courte": "Création de flyer stylisé pour l'événement « Full Black » à la Maison des Jeunes.",
        "description_longue": (
            "Création du flyer de l'événement « Full Black » à la Maison des Jeunes : ambiance sombre, "
            "lettrage doré en relief, dress code mis en avant et informations pratiques "
            "(date, horaires, prévente et tarif du jour, lieu, infoline)."
        ),
    },
    {
        "id": 10,
        "titre": "Affiche Timfa",
        "categorie": "Design Graphique",
        "image": "images/timfa.jpg",
        "affiche": True,
        "description_courte": "Conception publicitaire et visuelle pour la marque Timfa.",
        "description_longue": "Conception publicitaire et visuelle pour la marque Timfa.",
    },
    {
        "id": 11,
        "titre": "Affiche Miss / Événement Mode",
        "categorie": "Design Graphique",
        "image": "images/miss.jpg",
        "affiche": True,
        "description_courte": "Visuel élégant pour élection ou événement de mode.",
        "description_longue": "Visuel élégant pour élection ou événement de mode.",
    },
    {
        "id": 12,
        "titre": "Visuel Événementiel Rose",
        "categorie": "Design Graphique",
        "image": "images/event-rose.jpg",
        "affiche": True,
        "description_courte": "Création graphique aux tons roses pour communication digitale.",
        "description_longue": "Création graphique aux tons roses pour communication digitale.",
    },
    {
        "id": 13,
        "titre": "Visuel Automobile & Prestige",
        "categorie": "Design Graphique",
        "image": "images/auto.jpg",
        "affiche": True,
        "description_courte": "Affiche publicitaire orientée automobile et design haut de gamme.",
        "description_longue": "Affiche publicitaire orientée automobile et design haut de gamme.",
    },
    {
        "id": 4,
        "titre": "Portrait & Regard Urbain",
        "categorie": "Photographie",
        "image": "images/shooting-1.jpg",
        "portrait": True,
        "description_courte": "Portrait au regard intense dans un décor urbain.",
        "description_longue": "Portrait au regard intense dans un décor urbain, réalisé lors d'un shooting en extérieur.",
    },
    {
        "id": 5,
        "titre": "Immersion & Mode Streetwear",
        "categorie": "Photographie",
        "image": "images/shooting-2.jpg",
        "portrait": True,
        "description_courte": "Shooting mode streetwear en immersion dans la ville.",
        "description_longue": "Shooting mode streetwear en immersion dans la ville : attitude, tenues et cadrages dynamiques.",
    },
    {
        "id": 6,
        "titre": "Shooting Scène & Événementiel",
        "categorie": "Photographie",
        "image": "images/shooting-3.jpg",
        "portrait": True,
        "description_courte": "Photographie de scène et d'événement.",
        "description_longue": "Photographie de scène et d'événement : capter l'énergie et les moments forts sur le vif.",
    },
    {
        "id": 14,
        "titre": "Cliché Artistique & Lumière Naturelle",
        "categorie": "Photographie",
        "image": "images/shooting-4.jpg",
        "description_courte": "Cliché artistique travaillé en lumière naturelle.",
        "description_longue": "Cliché artistique travaillé en lumière naturelle, pour une image douce et authentique.",
    },
    {
        "id": 15,
        "titre": "Portrait Professionnel & Prestation",
        "categorie": "Photographie",
        "image": "images/shooting-5.jpg",
        "portrait": True,
        "description_courte": "Portrait professionnel soigné pour une prestation photo.",
        "description_longue": "Portrait professionnel soigné réalisé dans le cadre d'une prestation photo sur mesure.",
    },
    {
        "id": 16,
        "titre": "Ambiance de Groupe & Authenticité",
        "categorie": "Photographie",
        "image": "images/shooting-6.jpg",
        "description_courte": "Photo de groupe pleine d'ambiance et de spontanéité.",
        "description_longue": "Photo de groupe pleine d'ambiance et de spontanéité, qui garde l'authenticité du moment.",
    },
    {
        "id": 17,
        "titre": "Série Mode & Lifestyle",
        "categorie": "Photographie",
        "image": "images/shooting-7.jpg",
        "portrait": True,
        "description_courte": "Série photo mode et lifestyle.",
        "description_longue": "Série photo mode et lifestyle : style, poses naturelles et univers visuel cohérent.",
    },
    {
        "id": 18,
        "titre": "Regard Captivé & Expression",
        "categorie": "Photographie",
        "image": "images/shooting-8.jpg",
        "description_courte": "Portrait centré sur le regard et l'expression.",
        "description_longue": "Portrait centré sur le regard et l'expression, pour une image qui accroche.",
    },
    {
        "id": 7,
        "titre": "Couverture Événementielle & Défilé",
        "categorie": "Montage vidéo",
        "image": "images/vidéo-1.mp4",
        "video": True,
        "description_courte": "Captation et montage dynamique d'événement culturel et mode.",
        "description_longue": "Captation et montage dynamique d'événement culturel et mode.",
    },
    {
        "id": 8,
        "titre": "Spot Publicitaire & Brand Content",
        "categorie": "Montage vidéo",
        "image": "images/vidéo-2.mp4",
        "video": True,
        "description_courte": "Vidéo promotionnelle rythmée pour la mise en valeur de marque.",
        "description_longue": "Vidéo promotionnelle rythmée pour la mise en valeur de marque.",
    },
    {
        "id": 9,
        "titre": "Reel & Format Court TikTok / Instagram",
        "categorie": "Montage vidéo",
        "image": "images/vidéo-3.mp4",
        "video": True,
        "description_courte": "Montage dynamique optimisé pour l'engagement sur les réseaux sociaux.",
        "description_longue": "Montage dynamique optimisé pour l'engagement sur les réseaux sociaux.",
    },
    {
        "id": 19,
        "titre": "Immersion & Prestation Scénique",
        "categorie": "Montage vidéo",
        "image": "images/vidéo-4.mp4",
        "video": True,
        "description_courte": "Reportage et montage professionnel d'événements publics.",
        "description_longue": "Reportage et montage professionnel d'événements publics.",
    },
]
