# ==============================================================================
# FICHIER CENTRAL DE DONNÉES
# Mettez à jour ces listes pour modifier le contenu de votre site.
# ==============================================================================

TYPE_ACADEMIQUE = "Académique"
TYPE_PERSONNEL = "Personnel"
TYPE_PROFESSIONNEL = "Professionnel"

# URL de base pour les images pour ne pas avoir à le répéter
IMAGE_DIR = 'images/'

# Mes informations personnelles
ME = {
    "name": "Oumar BARRY",
    "headline": "Ingénieur en Génie Chimique & Développeur Python",
    "hero_intro": "Je conçois des solutions innovantes à l'intersection du génie des procédés et de la technologie, en transformant des défis industriels complexes en applications logicielles performantes.",
    "about_text": "Étudiant en 3ème année du cycle ingénieur, je suis passionné par l'optimisation des procédés industriels, particulièrement dans le secteur minier. Ma solide base en modélisation numérique et en thermodynamique, alliée à ma maîtrise d'outils comme Python, Maple et ANSYS, me permet de concevoir et d'analyser des solutions techniques efficaces. Je suis rigoureux, adaptable et toujours motivé à contribuer à des innovations durables.",
    "photo": IMAGE_DIR + "oumar_barry_photo.png",
    "cv_file": "cv/oumar_barry_cv.pdf"
}

PROJECTS = [
    {
        "title": "Portfolio Statique avec Flask",
        "type": TYPE_PERSONNEL,
        "short_description": "Création d'un portfolio web professionnel, généré comme un site statique via Flask pour des performances et une sécurité optimales.",
        "technologies": "Python, Flask, Frozen-Flask, Bootstrap 5",
        "image_file": IMAGE_DIR + "portfolio.png",
        "project_url": "https://github.com/oumarbarry/my-portfolio",
        "year": 2025,
    },
    {
        "title": "Simulation de Colonne de Distillation",
        "type": TYPE_ACADEMIQUE,
        "short_description": "Modélisation (McCabe-Thiele) d'une colonne binaire pour calculer flux, nombre d'étages et reflux minimal.",
        "technologies": "Python, Matplotlib, NumPy",
        "image_file": IMAGE_DIR + "distillation.webp",
        "project_url": "",
        "year": 2024,
    },
    {
        "title": "Dessalement Solaire par CFD",
        "type": TYPE_ACADEMIQUE,
        "short_description": "Conception 3D et simulation d'un concentrateur solaire pour le dessalement, validant la viabilité technico-économique du système.",
        "technologies": "ANSYS Fluent, Modélisation 3D, CFD",
        "image_file": IMAGE_DIR + "solaire_cfd.png",
        "project_url": "",
        "year": 2023,
    },
    # --- Ajoutez tous vos autres projets ici ---
]

SKILLS = {
    "Programmation & Logiciels": ["Python", "VB.NET", "C", "SQL", "Maple", "Matlab", "MS Office"],
    "Simulation & Modélisation": ["Aspen Plus", "ANSYS Fluent", "DWSIM", "Modélisation Thermodynamique", "Bilans Énergétiques"],
    "Compétences Techniques": ["Génie Chimique", "Optimisation des Procédés", "Efficacité Énergétique", "Transferts de Matière"],
    "Langues": ["Français (C1)", "Anglais (B1)", "Bambara (Natif)", "Arabe (Débutant)"],
    "Compétences Comportementales": ["Rigueur scientifique", "Autonomie", "Esprit d'équipe", "Curiosité", "Adaptabilité"]
}

RESUME = {
    "Éducation": [
        {
            "title": "Cycle Ingénieur - Procédés & Ingénierie Chimique",
            "institution": "FSTS, Settat",
            "period": "2023 - Présent",
            "description": "Moyenne des deux premières années : 15.33/20. Classé 1er et 2ème de promotion.",
            "logo": IMAGE_DIR + "fsts.png"
        },
        {
            "title": "DEUG - Sciences de la Terre et de l'Univers",
            "institution": "FS, Rabat",
            "period": "2021 - 2023",
            "description": "Obtenu avec Mention Très Bien (16.49/20).",
            "logo": IMAGE_DIR + "fsr.jpg"
        }
    ],
    "Expérience": [
        {
            "title": "Stage en Efficacité Énergétique",
            "institution": "OCP Group - Jorf Lasfar",
            "period": "Sept 2025 - Oct 2025",
            "description": "Analyse des consommations des utilités, identification de pertes évaluées à 72,9M MAD et proposition de plans d'amélioration.",
            "logo": IMAGE_DIR + "ocp.jpg"
        },
        # ... autres expériences ...
    ]
}