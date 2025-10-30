from flask_frozen import Freezer
from app import app  # On importe notre application depuis app.py

# V V V AJOUTEZ CETTE LIGNE CI-DESSOUS V V V
# Indique à Frozen-Flask l'URL de base de votre site sur GitHub Pages.
# Remplacez "barry-oumar" et "my-portfolio" par votre nom d'utilisateur et le nom de votre dépôt.
app.config['FREEZER_BASE_URL'] = 'https://barry-oumar.github.io/my-portfolio/'
# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

# Configure Frozen-Flask pour trouver les fichiers statiques
app.config['FREEZER_STATIC_IGNORE'] = []

freezer = Freezer(app)

if __name__ == '__main__':
    print("Freezing the application with correct base URL...")
    freezer.freeze()
    print("Application frozen successfully. Static site is in the 'build' folder.")