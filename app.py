from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from models import Hero, Power, HeroPower
    from routes import heroes_bp, powers_bp, hero_powers_bp
    app.register_blueprint(heroes_bp)
    app.register_blueprint(powers_bp)
    app.register_blueprint(hero_powers_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(port=5555, debug=True)
