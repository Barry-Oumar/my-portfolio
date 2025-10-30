# ==============================================================================
# CE FICHIER REMPLACE VOTRE BASE DE DONNÉES
# Mettez à jour ces listes pour modifier le contenu de votre site.
# ==============================================================================

PROJECTS = [

    {
        "id": 2,
        "title": "Chemical Process Simulator",
        "short_description": "Academic project to simulate industrial chemical processes using Python.",
        "technologies": "Python, NumPy, Matplotlib",
        "image_file": "distillation.webp",
        "project_url": "", # Laissez vide si c'est un projet sans lien
        "year": 2024,
        "lang": "en"
    },
    # --- Ajoutez tous vos autres projets ici ---
]

SKILLS = [
    {"category": "Programming", "name": "Python"},
    {"category": "Programming", "name": "SQL"},
    {"category": "Programming", "name": "HTML & CSS"},
    {"category": "Data", "name": "NumPy & Pandas"},
    {"category": "Data", "name": "Matplotlib"},
    {"category": "Process", "name": "Process Simulation"},
    {"category": "Process", "name": "Chemical Engineering"},
    {"category": "Soft", "name": "Problem Solving"},
    # --- Ajoutez toutes vos autres compétences ici ---
]

RESUME = {
    "Education": [
        {
            "id": 1,
            "entry_type": "Education",
            "title": "Master's in Chemical & Process Engineering",
            "institution": "FST Settat",
            "period": "2022 - 2024",
            "description": "Specialization in process control and optimization.",
            "logo": "fsts.png", # Mettez le logo dans static/images/
            "lang": "en"
        }
        # --- Ajoutez vos autres formations ici ---
    ],
    "Experience": [
        {
            "id": 1,
            "entry_type": "Experience",
            "title": "End of Studies Internship",
            "institution": "OCP Group - Jorf Lasfar",
            "period": "Feb 2024 - Jun 2024",
            "description": "Developed and implemented a monitoring system for industrial processes.",
            "logo": "ocp.jpg",
            "lang": "en"
        }
        # --- Ajoutez vos autres expériences ici ---
    ]
}