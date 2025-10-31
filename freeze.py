from flask_frozen import Freezer
from app import app

# VÉRIFIEZ ET CORRIGEZ CETTE URL AVEC VOTRE NOM D'UTILISATEUR ET NOM DE DÉPÔT
# EXEMPLE: app.config['FREEZER_BASE_URL'] = 'https://oumarbarry.github.io/my-portfolio/'
app.config['FREEZER_BASE_URL'] = 'https://barry-oumar.github.io/my-portfolio/'

# Important pour s'assurer que Frozen-Flask trouve bien tous les fichiers
app.config['FREEZER_STATIC_IGNORE'] = []

freezer = Freezer(app)

if __name__ == '__main__':
    print("Génération du site statique...")
    freezer.freeze()
    print("Site généré avec succès dans le dossier 'build'.")