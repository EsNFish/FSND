from backend.src.swagger.definitions.swagger_definitions import RecipeItemShort, DrinkShort, ResponseShort

get_drink_specs = {
    "definitions": {
        "RecipeItemShort": RecipeItemShort,
        "DrinkShort": DrinkShort,
        "ResponseShort": ResponseShort
    },
    "responses": {
        "200": {
            "description": "A response containing the recipes for all available drinks",
            "schema": {
                "$ref": "#/definitions/ResponseShort"
            }
        }
    }
}
