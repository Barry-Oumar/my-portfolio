# ==============================================================================
# PORTFOLIO - OUMAR BARRY

# ==============================================================================

# Informations personnelles
ME = {
    "name": "Oumar BARRY",
    "title": "Ingénieur Procédés & Génie Chimique",
    "subtitle": "Ingénieur Procédés Chimiques & Spécialiste Simulation",
    "tagline": "Je transforme des défis industriels complexes en solutions innovantes",
    "hero_description": "Bienvenue dans mon portfolio, où chaque projet raconte une histoire d'innovation et de rigueur technique. Rejoignez-moi pour explorer le monde vibrant de la simulation, de la modélisation et du développement, à travers mon expertise en génie des procédés.",
    "about_intro": "Passionné par l'optimisation des procédés industriels et la modélisation numérique.",
    "about_text": "Ingénieur en procédés chimiques, je suis passionné par l'optimisation et la simulation des procédés industriels. Ma solide base en modélisation numérique, modélisation des procédés et en thermodynamique, alliée à ma maîtrise d'outils comme Python, MATLAB, Maple et ANSYS Fluent, me permet de concevoir et d'analyser des solutions techniques efficaces.",
    "email": "oumarbarry75271687@gmail.com",
    "phone": "+212 6 46 49 88 12",
    "location": "Settat, Maroc",
    "photo": "images/oumar_barry_photo.webp",
    "cv_file": "cv/oumar_barry_cv.pdf",
    "linkedin": "https://www.linkedin.com/in/oumar-barry-0876a12a3",
    "github": "https://github.com/Barry-Oumar",
}

# Compétences organisées par catégories
SKILLS = {
    "Langages de Programmation": [
        "Python", "MATLAB", "SQL", "HTML/CSS", "vb.net",
    ],
    "Outils de Simulation": [
       "Aspen Plus", "Aspen HYSYS","DWSIM", "ANSYS Fluent", "Maple", "COMSOL Multiphysics"
    ],
    "Frameworks & Bibliothèques": [
        "Flask", "NumPy", "Pandas", "Matplotlib", "SciPy"
    ],
    "Compétences Techniques": [
        "Modélisation CFD", "Thermodynamique", "Transfert de chaleur",
        "Distillation", "Optimisation de procédés", "Analyse de données", "amélioration continue"
    ],
    "Outils de Développement": [
       "GitHub", "VS Code", "Jupyter Notebook", "LaTeX"
    ]
}

# Processus de travail (inspiré de "From Consultation to Captivating Imagery")
PROCESS_STEPS = [
    {
        "number": "01",
        "title": "Analyse du Problème",
        "description": "Je commence par une compréhension approfondie du problème industriel ou académique. Cette approche collaborative garantit que chaque solution répond aux besoins spécifiques.",
        "icon": "bi-search"
    },
    {
        "number": "02",
        "title": "Modélisation & Simulation",
        "description": "Ensemble, en travaillant étroitement, nous créons des modèles qui reflètent fidèlement le système étudié. En combinant théorie et pratique, nous développons des simulations précises et significatives.",
        "icon": "bi-cpu"
    },
    {
        "number": "03",
        "title": "Optimisation & Analyse",
        "description": "Après la simulation, j'analyse les résultats pour identifier les opportunités d'optimisation et garantir que les performances correspondent aux objectifs fixés.",
        "icon": "bi-graph-up-arrow"
    },
    {
        "number": "04",
        "title": "Documentation & Livraison",
        "description": "Que ce soit pour promouvoir une innovation ou simplement documenter un processus, je m'assure que lorsque vous recevez le livrable final, vous voyez clairement la valeur ajoutée.",
        "icon": "bi-file-earmark-check"
    }
]

# Projets
PROJECTS = [
    {
        "id": 2,
        "title": "Simulation de Colonne de Distillation",
        "category": "Simulation",
        "year": 2024,
        "short_description": "Modélisation McCabe-Thiele d'une colonne binaire pour calculer le nombre de plateaux théoriques.",
        "full_description": "Développement d'un outil Python de simulation de colonnes de distillation binaire basé sur la méthode graphique de McCabe-Thiele. L'application permet de déterminer le nombre de plateaux théoriques nécessaires pour une séparation donnée.",
        "technologies": ["Python", "Matplotlib", "NumPy", "Thermodynamique"],
        "image_file": "images/distillation.webp",
        "project_url": "https://github.com/oumarbarry/distillation-column",
        "featured": True
    },
    {
        "id": 3,
        "title": "Modèle UNIFAC en Python",
        "category": "Modélisation",
        "year": 2024,
        "short_description": "Implémentation du modèle UNIFAC pour prédire les coefficients d'activité dans les mélanges liquides.",
        "full_description": "Création d'une bibliothèque Python complète implémentant le modèle UNIFAC (UNIQUAC Functional-group Activity Coefficients) pour la prédiction des propriétés thermodynamiques des mélanges non-idéaux.",
        "technologies": ["Python", "Pandas", "SciPy", "Thermodynamique"],
        "image_file": "images/unifac.png",
        "project_url": None,
        "featured": True
    },
    {
        "id": 4,
        "title": "Simulation CFD d'un Collecteur Solaire",
        "category": "Simulation",
        "year": 2024,
        "short_description": "Analyse CFD du transfert thermique dans un collecteur solaire thermique.",
        "full_description": "Simulation numérique complète d'un collecteur solaire plan utilisant ANSYS Fluent. Le projet inclut l'analyse du champ de température, du flux thermique et de l'efficacité du collecteur sous différentes conditions d'ensoleillement.",
        "technologies": ["ANSYS Fluent", "CFD", "Transfert thermique", "Énergies renouvelables"],
        "image_file": "images/solaire_cfd.png",
        "project_url": None,
        "pdf_file": "docs/rapport_collecteur_solaire.pdf",
        "featured": False
    },
    {
        "id": 5,
        "title": "Résolution d'EDP par Différences Finies",
        "category": "Calcul Numérique",
        "year": 2024,
        "short_description": "Implémentation de méthodes numériques pour résoudre des équations aux dérivées partielles.",
        "full_description": "Développement d'outils numériques en Python et MATLAB pour résoudre des EDP par la méthode des différences finies. Application à l'équation de la chaleur et à l'équation de diffusion.",
        "technologies": ["Python", "MATLAB", "NumPy", "Analyse numérique"],
        "image_file": "images/finite_difference.JPG",
        "project_url": None,
        "pdf_file": "docs/rapport_differences_finies.pdf",
        "featured": False
    }
]

# Expérience professionnelle & Stages
EXPERIENCE = [
    {
        "title": "Stage Technique",
        "institution": "Office Chérifien des Phosphates (OCP)",
        "period": "Été 2024",
        "description": "Stage d'observation et d'apprentissage dans une unité de production de phosphates at Khouribga. Analyse des procédés de traitement et d'enrichissement des minerais.",
        "logo": "images/ocp.jpg"
    }
]

# Engagement & Activités
VOLUNTEERING = [
    {
        "title": "Enseignant de FLE (Français Langue Étrangère)",
        "institution": "Preply (Plateforme en ligne)",
        "period": "Oct 2023 - Présent",
        "description": "Enseignement du français à des étudiants internationaux. Création de plans de cours personnalisés et suivi des progrès linguistiques.",
        "logo": "images/preply.webp"
    },
    {
        "title": "Interprète bilingue",
        "institution": "UNHCR (Organisation des Nations Unies pour les Réfugiés)",
        "period": "2022 - 2023",
        "description": "Interprétation bilingue (Bambara-français) pour les réfugiés et les migrants.",
        "logo": "images/unhcr.png"
    }
]

# Formation
EDUCATION = [
    {
        "title": "Cycle Ingénieur - Génie des Procédés",
        "institution": "Faculté des Sciences et Techniques de Settat (FSTS)",
        "period": "2023 - 2026 (en cours)",
        "description": "Formation d'ingénieur spécialisée en génie chimique et des procédés. Cours avancés en thermodynamique, transfert de matière et chaleur, simulation de procédés, et modélisation CFD.",
        "logo": "images/fsts.png"
    },
    {
        "title": "DEUG en Sciences de Terre et de l'Univers",
        "institution": "Faculté des Sciences et de la Rabat (FSR)",
        "period": "2021 - 2023",
        "description": "Cursus approfondi en géologie, couvrant la gestion des risques naturels, les ressources en eau, la prospection minière et l'environnement. ",
        "logo": "images/fsr.jpg"
    }
]

# Services (adapté de mon profil)
SERVICES = [
    {
        "title": "Simulation & Modélisation",
        "description": "Développement de modèles numériques et simulations CFD pour l'analyse et l'optimisation de procédés industriels.",
        "icon": "bi-cpu-fill"
    },
    {
        "title": "Développement Python",
        "description": "Création d'applications scientifiques, d'outils d'analyse de données et d'interfaces web avec Python et ses bibliothèques.",
        "icon": "bi-code-slash"
    },
    {
        "title": "Analyse de Données",
        "description": "Traitement et visualisation de données techniques, analyse statistique et création de rapports automatisés.",
        "icon": "bi-graph-up"
    },
    {
        "title": "Optimisation de Procédés",
        "description": "Application de méthodes d'optimisation pour améliorer l'efficacité énergétique et la productivité des procédés.",
        "icon": "bi-lightning-charge-fill"
    }
]
