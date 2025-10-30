from flask_frozen import Freezer
from app import app

# VÉRIFIEZ CETTE LIGNE TRÈS ATTENTIVEMENT
# Est-ce que votre nom d'utilisateur est bien "barry-oumar" ?
# Est-ce que le nom de votre dépôt est bien "my-portfolio" ?
app.config['FREEZER_BASE_URL'] = 'https://barry-oumar.github.io/my-portfolio/'

app.config['FREEZER_STATIC_IGNORE'] = []
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()