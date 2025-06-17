from flask import Blueprint, request, jsonify
from .models import Hero, Power, HeroPower
from .extensions import db

api = Blueprint('api', __name__)

# Welcome route
@api.route('/')
def index():
    return jsonify({"message": "Welcome to Superheroes API 💥"})

# GET /heroes
@api.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

# POST /heroes
@api.route('/heroes', methods=['POST'])
def create_hero():
    data = request.get_json()

    if not data.get('name') or not data.get('super_name'):
        return jsonify({'error': 'Both name and super_name are required'}), 400

    hero = Hero(name=data['name'], super_name=data['super_name'])
    db.session.add(hero)
    db.session.commit()

    return jsonify(hero.to_dict()), 201
