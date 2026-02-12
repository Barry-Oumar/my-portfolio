from flask_frozen import Freezer
from app import app
import mimetypes

# Configuration pour le build local
app.config['FREEZER_BASE_URL'] = '/'

# Important pour s'assurer que Frozen-Flask trouve bien tous les fichiers
app.config['FREEZER_STATIC_IGNORE'] = []
app.config['FREEZER_RELATIVE_URLS'] = True

mimetypes.add_type('image/webp', '.webp')

freezer = Freezer(app)

if __name__ == '__main__':
    print("Génération du site statique...")
    freezer.freeze()