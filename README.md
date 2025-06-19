# superheroes-api
Flask API -superheroe
# 🦸‍♂️ Superheroes API

A Flask-based RESTful API for managing Superheroes, their Powers, and how they relate using HeroPowers. Built for Phase 4 assessment with full validations, associations, and CRUD operations.

---

##  Features

- Full CRUD for HeroPowers
- Read-only endpoints for Heroes and Powers
- Validations for strength values
- Many-to-many relationship between Heroes and Powers with extra attribute `strength`
- JSON responses with proper error handling

---

## 🛠️ Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Marshmallow 
- SQLite (default DB)
- Alembic (for migrations)

---

##  Models Overview

### 🦸 Hero

- `id`: integer (Primary Key)
- `name`: string
- `super_name`: string

Relationships:
- Has many `HeroPower`
- Has many `Power` through `HeroPower`

---

###  Power

- `id`: integer 
- `name`: string
- `description`: string _(must be at least 20 characters)_

Relationships:
- Has many `HeroPower`
- Has many `Hero` through `HeroPower`

---

###  HeroPower

- `id`: integer (Primary Key)
- `strength`: string _(must be either `"Strong"`, `"Weak"` or `"Average"` only)_
- `hero_id`: ForeignKey
- `power_id`: ForeignKey

Represents the relationship between a Hero and a Power with an additional attribute `strength`.

---

## 🔀 API Endpoints

### GET /heroes
Returns a list of all heroes (id, name, super_name)

### GET /heroes/:id
Returns full hero data with powers
- 404 error if not found

### GET /powers
Returns all powers

### GET /powers/:id
Returns a specific power
- 404 error if not found

### PATCH /powers/:id
Update a power (only description allowed)
- 400 if validation fails

### POST /hero_powers
Assigns a power to a hero
- Requires `strength`, `hero_id`, `power_id`
- Returns the hero with updated powers
- 400 if strength is invalid or any data is missing

---

##  How to Run Locally

```bash
git clone https://github.com/yourusername/superheroes-api.git
cd superheroes-api
pipenv install
pipenv shell
pipenv install flask flask_sqlalchemy flask_migrate   (if pip show flask. got nothing)
flask db init
flask db migrate -m "Initial"
flask db upgrade
python seed.py
flask run


# Tree

├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── app
│   ├── __init__.py
│   ├── extensions.py
│   ├── models.py
│   ├── routes.py
│   └── validations
├── app.py
├── config.py
├── instance
│   └── superheroes.db
├── manage.py
├── migrations
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── 58dd370eb710_setup.py
│       └── 93f29634f1c7_initial_models.py
├── requirements.txt
└── seed.py
