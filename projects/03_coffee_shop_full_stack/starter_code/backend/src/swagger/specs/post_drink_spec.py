from backend.src.swagger.definitions.swagger_definitions import ResponseLong, RecipeItemLong, DrinkLong, DrinkLongNoId, \
    error_builder

post_drink_specs = {
    "parameters": [
        {
            "name": "drink",
            "description": "Need both recipe and title to create",
            "in": "body",
            "type": "object",
            "schema": {
                "$ref": "#/definitions/DrinkLongNoId"
            },
            "required": "true"
        }
    ],
    "definitions": {
        "RecipeItemLong": RecipeItemLong,
        "DrinkLong": DrinkLong,
        "DrinkLongNoId": DrinkLongNoId,
        "ResponseLong": ResponseLong,
        "Error401": error_builder(401, 'Authentication token has expired'),
        "Error403": error_builder(403, 'User is missing permissions'),
        "Error404": error_builder(404, "Drink does not exist"),
        "Error422": error_builder(422, "Missing data in the request")
    },
    "responses": {
        "200": {
            "description": "A response containing an array with the new drink added",
            "schema": {
                "$ref": "#/definitions/ResponseLong"
            }
        },
        "400": {
            "description": "Error when JWT token cannot be parsed",
            "schema": {
                "$ref": "#/definitions/Error400"
            }
        },
        "401": {
            "description": "Error when JWT token is expired",
            "schema": {
                "$ref": "#/definitions/Error401"
            }
        },
        "403": {
            "description": "Error when user does not have proper permissions",
            "schema": {
                "$ref": "#/definitions/Error403"
            }
        },
        "422": {
            "description": "Error Thrown when data is missing from the body of the request",
            "schema": {
                "$ref": "#/definitions/Error422"
            }
        }
    }
}
