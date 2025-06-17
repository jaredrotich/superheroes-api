
from flask import Flask
from .extensions import db, migrate
from .routes import api

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api, url_prefix="/")

    from . import models  

    return app
