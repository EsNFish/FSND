import json

from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError

from .auth.auth import requires_auth
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


'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''

'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''

# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": error.description
    }), 422


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''


@app.errorhandler(403)
def handle_403(error):
    return jsonify({
        "success": False,
        "error": 403,
        "message": error.description
    }), 403


'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''
