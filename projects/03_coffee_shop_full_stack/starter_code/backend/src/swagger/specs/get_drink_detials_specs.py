from backend.src.swagger.definitions.swagger_definitions import RecipeItemLong, DrinkLong, ResponseLong, error_builder

get_drink_details_specs = {
    "definitions": {
        "RecipeItemLong": RecipeItemLong,
        "DrinkLong": DrinkLong,
        "ResponseLong": ResponseLong,
        "Error400": error_builder(400, 'Unable to parse authentication token'),
        "Error401": error_builder(401, 'Authentication token has expired'),
        "Error403": error_builder(403, 'User is missing permissions'),
    },
    "responses": {
        "200": {
            "description": "A response containing complete info for all available drinks",
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
        }
    }
}
