from backend.src.swagger.definitions.swagger_definitions import error_builder

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
        "Error400": error_builder(400, 'Unable to parse authentication token'),
        "Error401": error_builder(401, 'Authentication token has expired'),
        "Error403": error_builder(403, 'User is missing permissions'),
        "Error404": error_builder(404, "Drink does not exist")
    },
    "responses": {
        "200": {
            "description": "Returns the id of the deleted drink",
            "schema": {
                "$ref": "#/definitions/DeleteSuccess"
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
        "404": {
            "description": "Error when drink id to delete doesn't exist",
            "schema": {
                "$ref": "#/definitions/Error404"
            }
        }
    }
}
