#Je définis ce fichier pour fixer toutes les routes possibles à l'utilisateur
from flask import render_template
from website import app
from website.dataready import *

#J'utilise un décorateur
@app.route('/', endpoint='main_home') 
# / represente l'URL de la page d'accueil, toutes les fonctions au dessous du decorateur seront executées uniquement lorque l'utilisateur
# accede à l'URL associé, qui sera / pour notre cas.
def home():



    return render_template('index.html')




