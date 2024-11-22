# Importations de la fonctionalité annotations pour faciliter les annotations
# de type
from __future__ import annotations
# Modules centraux
import os
import shutil

### Modules secondaires, tiers
# Réponses web
from flask import Flask, render_template, redirect, url_for, session, request
# Base de donnée
from flask_sqlalchemy import SQLAlchemy
# Sécurité et criptage des mots de passe
from werkzeug.security import generate_password_hash, check_password_hash


# Modules tertiaires, locaux


# Setup
app = Flask(__name__)

app.secret_key = 'MyOwnSuperSecretKeyThatNoOneElseShouldKnow'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


# Constantes
DEBUG = True

##############################################################################
# Database                                                                   #
##############################################################################

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(100))
    pseudo = db.column(db.String(100))
    password = db.column(db.String(200))


##############################################################################
# Routes                                                                     #
##############################################################################

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/login')
def login():
    pseudo = request.form["pseudo"]
    mail = request.form["email"]


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=DEBUG)







