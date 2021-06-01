from backend.src.swagger.definitions.swagger_definitions import ResponseLong, RecipeItemLong, DrinkLong, DrinkLongNoId, \
    Error400, Error404

patch_drink_specs = {
    "parameters": [
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
        "Error400": Error400,
        "Error404": Error404
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
        "404": {
            "description": "Error thrown when drink to update does not exist",
            "schema": {
                "$ref": "#/definitions/Error404"
            }
        }
    }
}
