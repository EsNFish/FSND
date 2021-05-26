from backend.src.swagger.definitions.swagger_definitions import RecipeItem, Drink, Response

get_drink_specs = {
  "definitions": {
      "RecipeItem": RecipeItem,
      "Drink": Drink,
      "Response": Response
  },
  "responses": {
    "200": {
      "description": "A response containing the recipes for all available drinks",
      "schema": {
          "$ref": "#/definitions/Response"
      }
    }
  }
}