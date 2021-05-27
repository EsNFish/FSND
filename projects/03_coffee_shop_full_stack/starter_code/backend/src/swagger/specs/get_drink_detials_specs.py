from backend.src.swagger.definitions.swagger_definitions import RecipeItemLong, DrinkLong, ResponseLong

get_drink_details_specs = {
  "definitions": {
      "RecipeItemLong": RecipeItemLong,
      "DrinkLong": DrinkLong,
      "ResponseLong": ResponseLong
  },
  "responses": {
    "200": {
      "description": "A response containing complete info for all available drinks",
      "schema": {
          "$ref": "#/definitions/ResponseLong"
      }
    }
  }
}