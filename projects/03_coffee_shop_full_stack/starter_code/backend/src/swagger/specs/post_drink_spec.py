from backend.src.swagger.definitions.swagger_definitions import ResponseLong, RecipeItemLong, DrinkLong, DrinkLongNoId

post_drink_specs = {
    "parameters": [
        {
            "name": "drink",
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
        "ResponseLong": ResponseLong
    },
    "responses": {
        "200": {
            "description": "A response containing an array with the new drink added",
            "schema": {
                "$ref": "#/definitions/ResponseLong"
            }
        }
    }
}
