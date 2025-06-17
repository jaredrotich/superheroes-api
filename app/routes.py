from flask import Blueprint, request, jsonify
from .models import Hero, Power, HeroPower
from .extensions import db

api = Blueprint('api', __name__)

# Welcome Route
@api.route('/')
def index():
    return jsonify({"message": "Welcome to Superheroes API 💥"})


# GET /heroes
@api.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([
        {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        } for hero in heroes
    ])


# GET /heroes/:id
@api.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "hero_powers": [
            {
                "id": hp.id,
                "hero_id": hp.hero_id,
                "power_id": hp.power_id,
                "strength": hp.strength,
                "power": {
                    "id": hp.power.id,
                    "name": hp.power.name,
                    "description": hp.power.description
                }
            } for hp in hero.hero_powers
        ]
    })


# GET /powers
@api.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([
        {
            "id": power.id,
            "name": power.name,
            "description": power.description
        } for power in powers
    ])


# GET /powers/:id
@api.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    return jsonify({
        "id": power.id,
        "name": power.name,
        "description": power.description
    })


# PATCH /powers/:id
@api.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    description = data.get("description")

    if not description or len(description) < 20:
        return jsonify({"errors": ["validation errors"]}), 400

    power.description = description
    db.session.commit()

    return jsonify({
        "id": power.id,
        "name": power.name,
        "description": power.description
    })


# POST /hero_powers
@api.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    strength = data.get("strength")
    power_id = data.get("power_id")
    hero_id = data.get("hero_id")

    if strength not in ["Strong", "Weak", "Average"]:
        return jsonify({"errors": ["validation errors"]}), 400

    power = Power.query.get(power_id)
    hero = Hero.query.get(hero_id)

    if not power or not hero:
        return jsonify({"errors": ["validation errors"]}), 400

    hero_power = HeroPower(
        strength=strength,
        power_id=power_id,
        hero_id=hero_id
    )
    db.session.add(hero_power)
    db.session.commit()

    return jsonify({
        "id": hero_power.id,
        "hero_id": hero.id,
        "power_id": power.id,
        "strength": strength,
        "hero": {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        },
        "power": {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
    }), 201
