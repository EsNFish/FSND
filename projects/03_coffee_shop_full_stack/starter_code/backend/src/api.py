import json

from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError

from .auth.auth import requires_auth, AuthError
from .database.models import db_drop_and_create_all, setup_db, Drink

app = Flask(__name__)
setup_db(app)
CORS(app)

db_drop_and_create_all()


# ROUTES
@app.route('/drinks')
def get_drinks():
    available_drinks = [drink.short() for drink in Drink.query.all()]
    return jsonify({
        "success": True,
        'drinks': available_drinks
    })


@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def get_drink_details(auth_token):
    available_drinks_details = [drink.long() for drink in Drink.query.all()]
    return jsonify({
        "success": True,
        'drinks': available_drinks_details
    })


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def post_drink(auth_token):
    data = request.json

    if 'title' not in data or 'recipe' not in data:
        abort(422, "Missing data in the request")

    created_drink = Drink(
        title=data['title'],
        recipe=json.dumps(data['recipe'])
    )

    try:
        created_drink.insert()
    except IntegrityError:
        abort(422, "Drink already exists in database")

    return jsonify({
        "success": True,
        "drinks": [created_drink.long()]
    })


@app.route('/drinks/<drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(auth_token, drink_id):
    patched_drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

    if patched_drink is None:
        abort(404, 'Drink to update does not exist')

    drink_data = request.json

    if 'title' in drink_data:
        patched_drink.title = drink_data['title']
    if 'recipe' in drink_data:
        recipe = drink_data['recipe']
        patched_drink.recipe = recipe if type(recipe) == str else json.dumps(recipe)

    patched_drink.update()

    return jsonify({
        "success": True,
        "drinks": [patched_drink.long()]
    })


@app.route('/drinks/<drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(auth_token, drink_id):
    deleted_drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

    if deleted_drink is None:
        abort(404, 'Drink to delete does not exist')
    deleted_drink.delete()

    return jsonify({
        'success': True,
        'delete': drink_id
    })


# Error Handling
@app.errorhandler(404)
def handle_404(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": error.description
    }), 404


@app.errorhandler(422)
def handle_422(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": error.description
    }), 422


@app.errorhandler(AuthError)
def handle_auth_error(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error
    }), error.status_code
