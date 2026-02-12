from flask_frozen import Freezer
from app import app
import mimetypes

# Configuration pour GitHub Pages
# Important: GitHub Pages sert le site à /my-portfolio/ (nom du repo)
app.config['FREEZER_BASE_URL'] = 'https://barry-oumar.github.io/my-portfolio/'
app.config['FREEZER_DESTINATION'] = 'build'

# Important pour s'assurer que Frozen-Flask trouve bien tous les fichiers
app.config['FREEZER_STATIC_IGNORE'] = []
app.config['FREEZER_RELATIVE_URLS'] = True

mimetypes.add_type('image/webp', '.webp')

freezer = Freezer(app)

if __name__ == '__main__':
    print("Génération du site statique...")
    freezer.freeze()