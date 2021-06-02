from backend.src.swagger.definitions.swagger_definitions import ResponseLong, RecipeItemLong, DrinkLong, DrinkLongNoId, \
    error_builder

patch_drink_specs = {
    "parameters": [
        {
            "in": "path",
            "name": "drink_id",
            "required": True,
            "description": "id of drink to update"
        },
        {
            "name": "drink",
            "description": "Need at least one title or name to update",
            "in": "body",
            "type": "object",
            "schema": {
                "$ref": "#/definitions/DrinkLongNoId"
            }
        }
    ],
    "definitions": {
        "RecipeItemLong": RecipeItemLong,
        "DrinkLong": DrinkLong,
        "DrinkLongNoId": DrinkLongNoId,
        "ResponseLong": ResponseLong,
        "Error400": error_builder(400, "Missing request body"),
        "Error401": error_builder(401, 'Authentication token has expired'),
        "Error403": error_builder(403, 'User is missing permissions'),
        "Error404": error_builder(404, "Drink does not exist")
    },
    "responses": {
        "200": {
            "description": "A response containing an array with the drink with the new data",
            "schema": {
                "$ref": "#/definitions/ResponseLong"
            }
        },
        "400": {
            "description": "Error thrown when either no request body at all or request body is empty object",
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
        "404": {
            "description": "Error thrown when drink to update does not exist",
            "schema": {
                "$ref": "#/definitions/Error404"
            }
        }
    }
}
