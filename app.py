import os
from flask import Flask, render_template, url_for, send_from_directory, g
# On importe nos données locales depuis data.py
from data import PROJECTS, SKILLS, RESUME

app = Flask(__name__)

# Logique de langue (simplifiée, car il n'y a plus de session)
@app.before_request
def set_language():
    # Pour un site statique, la langue est généralement gérée par des URLs différentes
    # ou par le navigateur. Nous allons garder une logique simple pour la génération.
    g.lang = "en" # Langue par défaut pour la génération

# ==================================
# ==== ROUTES PUBLIQUES ====
# ==================================

@app.route("/")
def index():
    """Homepage"""
    featured_projects = sorted(PROJECTS, key=lambda p: p['year'], reverse=True)[:6]
    return render_template("index.html", projects=featured_projects, skills=SKILLS)

@app.route("/projects/")
def projects():
    """Full project gallery"""
    all_projects = sorted(PROJECTS, key=lambda p: p['year'], reverse=True)
    return render_template("projects.html", projects=all_projects)

@app.route("/resume/")
def resume():
    """Resume page showing education and experience"""
    return render_template("resume.html", 
                           education=RESUME["Education"], 
                           experience=RESUME["Experience"], 
                           skills=SKILLS)

@app.route("/about/")
def about():
    """About Me page"""
    skills_by_category = {}
    for skill in SKILLS:
        cat = skill["category"]
        if cat not in skills_by_category:
            skills_by_category[cat] = []
        skills_by_category[cat].append(skill["name"])
    return render_template("about.html", skills_by_category=skills_by_category)

@app.route("/contact/")
def contact():
    """Contact page with mailto link"""
    # Plus de formulaire, juste des informations de contact
    return render_template("contact.html")

@app.route('/download/oumar_barry_cv.pdf')
def download_cv_file(): # Changez aussi le nom de la fonction pour éviter toute confusion
    """Provide the CV file for download."""
    return send_from_directory('static/cv', 'oumar_barry_cv.pdf', as_attachment=True)

# ==================================
# ==== GESTION DES ERREURS ====
# ==================================

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page"""
    return render_template("404.html"), 404

# Le 500 n'est pas vraiment pertinent pour un site statique, mais on le garde pour le dev
@app.errorhandler(500)
def internal_error(e):
    return "<h1>500 - Internal Server Error</h1>", 500