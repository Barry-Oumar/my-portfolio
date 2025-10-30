# Changez "flask_Frozen" par "flask_frozen" tout en minuscules
from flask_frozen import Freezer

from app import app  # On importe notre application depuis app.py

# Configure Frozen-Flask pour trouver les fichiers statiques
app.config['FREEZER_STATIC_IGNORE'] = []

freezer = Freezer(app)

if __name__ == '__main__':
    print("Freezing the application...")
    freezer.freeze()
    print("Application frozen successfully. Static site is in the 'build' folder.")