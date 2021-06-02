import json

from werkzeug.exceptions import BadRequest
from flasgger import Swagger, swag_from
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError

from backend.src.swagger.specs.get_drink_detials_specs import get_drink_details_specs
from backend.src.swagger.specs.get_drink_spec import get_drink_specs
from backend.src.swagger.specs.post_drink_spec import post_drink_specs
from .auth.auth import requires_auth, AuthError
from .database.models import db_drop_and_create_all, setup_db, Drink
from .swagger.specs.delete_drink_spec import delete_drink_details_specs
from .swagger.specs.patch_drink_specs import patch_drink_specs

app = Flask(__name__)
setup_db(app)
CORS(app)
app.config['SWAGGER'] = {
    'title': "Coffee Shop"
}
swagger = Swagger(app)

db_drop_and_create_all()


# ROUTES
@app.route('/drinks')
@swag_from(get_drink_specs)
def get_drinks():
    """Public endpoint to get all available drinks"""
    available_drinks = [drink.short() for drink in Drink.query.all()]
    return jsonify({
        "success": True,
        'drinks': available_drinks
    })


@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
@swag_from(get_drink_details_specs)
def get_drink_details(auth_token):
    """Endpoint for Baristas and Managers to get detailed info about drinks"""
    available_drinks_details = [drink.long() for drink in Drink.query.all()]
    return jsonify({
        "success": True,
        'drinks': available_drinks_details
    })


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
@swag_from(post_drink_specs)
def post_drink(auth_token):
    """Endpoint for manager to add a new drink"""
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
@swag_from(patch_drink_specs)
@requires_auth('patch:drinks')
def update_drink(auth_token, drink_id):
    """Endpoint for manager to update an existing drink"""
    patched_drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

    if patched_drink is None:
        abort(404, 'Drink to update does not exist')

    drink_data = None
    try:
        drink_data = request.json
    except BadRequest:
        abort(400, "Missing request body")

    if drink_data is None or 'title' not in drink_data and 'recipe' not in drink_data:
        abort(400, "Need to pass in a value to update")
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
@swag_from(delete_drink_details_specs)
@requires_auth('delete:drinks')
def delete_drink(auth_token, drink_id):
    """Endpoint for manager to delete an existing drink"""
    deleted_drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

    if deleted_drink is None:
        abort(404, 'Drink to delete does not exist')
    deleted_drink.delete()

    return jsonify({
        'success': True,
        'delete': drink_id
    })


# Error Handling
@app.errorhandler(400)
def handle_400(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": error.description
    }), 400


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
