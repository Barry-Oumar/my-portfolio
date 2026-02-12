from flask import Flask, render_template
from flask_frozen import Freezer

# Import data
# Import data
from utils.data import (
    ME, SKILLS, PROJECTS, EXPERIENCE, EDUCATION, 
    SERVICES, PROCESS_STEPS, VOLUNTEERING
)

app = Flask(__name__)

# Note: Configuration Freezer est maintenant dans freeze.py uniquement

# Helper function to get featured projects
def get_featured_projects():
    return [p for p in PROJECTS if p.get('featured', False)]

# Routes
@app.route('/')
def index():
    return render_template(
        'index.html',
        me=ME,
        featured_projects=get_featured_projects(),
        skills=SKILLS,
        services=SERVICES,
        process_steps=PROCESS_STEPS,
        projects=PROJECTS
    )

@app.route('/projects/')
def projects():
    return render_template(
        'projects.html',
        me=ME,
        projects=PROJECTS
    )

@app.route('/services/')
def services():
    return render_template(
        'services.html',
        me=ME,
        services=SERVICES,
        process_steps=PROCESS_STEPS
    )

@app.route('/parcours/')
def parcours():
    return render_template(
        'parcours.html',
        me=ME,
        skills=SKILLS,
        experience=EXPERIENCE,
        volunteering=VOLUNTEERING,
        education=EDUCATION,
        projects=PROJECTS
    )

@app.route('/contact/')
def contact():
    return render_template(
        'contact.html',
        me=ME
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', me=ME), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
