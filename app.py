from flask import Flask, render_template, url_for, g
# On importe toutes nos données depuis data.py
from data import ME, PROJECTS, SKILLS, RESUME

app = Flask(__name__)

# Contexte global pour passer des informations à tous les templates
@app.context_processor
def inject_global_vars():
    return {
        "me": ME,
        "projects": PROJECTS,
        "skills": SKILLS,
        "resume": RESUME
    }

# ==================================
# ==== ROUTES PUBLIQUES ====
# ==================================

@app.route("/")
def index():
    featured_projects = sorted(PROJECTS, key=lambda p: p['year'], reverse=True)[:3]
    return render_template("index.html", featured_projects=featured_projects)

@app.route("/projects/")
def projects():
    all_projects = sorted(PROJECTS, key=lambda p: p['year'], reverse=True)
    return render_template("projects.html", projects=all_projects)

@app.route("/resume/")
def resume():
    return render_template("resume.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/about/")
def about():
    # 'about.html' a été fusionné dans 'index.html' et 'resume.html'.
    # Si vous voulez une page 'À Propos' dédiée, créez-la et décommentez.
    # Pour l'instant, on redirige vers l'accueil.
    return render_template("resume.html")

# ==================================
# ==== GESTION DES ERREURS ====
# ==================================

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404