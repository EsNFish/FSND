from backend.src.swagger.definitions.swagger_definitions import Error404

delete_drink_details_specs = {
    "parameters": [
        {
            "in": "path",
            "name": "drink_id",
            "required": True,
            "description": "id of drink to update"
        }
    ],
    "definitions": {
        "DeleteSuccess": {
            "type": "object",
            "properties": {
                "delete": {
                    "type": "string",
                    "example": "1"
                },
                "success": {
                    "type": "boolean",
                    "example": True
                }
            }
        },
        "Error404": Error404
    },
    "responses": {
        "200": {
            "description": "Returns the id of the deleted drink",
            "schema": {
                "$ref": "#/definitions/DeleteSuccess"
            }
        },
        "404": {
            "description": "Error when drink id to delete doesn't exist",
            "schema": {
                "$ref": "#/definitions/Error404"
            }
        }
    }
}
