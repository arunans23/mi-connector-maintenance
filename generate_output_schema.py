import os
import json
import argparse

def create_output_schema(is_rest_api_connector, operation_name):
    """
    Generate a basic output schema with payload, headers, and attributes.
    Includes the operation name in the title and description.
    """
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "title": f"Output Schema for {operation_name} Operation",
        "description": f"Output schema for the {operation_name} operation in the connector.",
        "properties": {
            "payload": {
                "type": "object",
                "description": f"The main response payload from the {operation_name} operation."
            },
            "headers": {
                "type": "object",
                "description": f"Transport headers returned by the {operation_name} operation.",
                "additionalProperties": True
            },
            "attributes": {
                "type": "object",
                "description": f"Metadata about the {operation_name} operation.",
                "properties": {},
                "additionalProperties": False
            }
        },
        "required": ["payload", "headers", "attributes"],
        "additionalProperties": False
    }
    
    # Add statusCode if it's a REST API-based connector
    if is_rest_api_connector:
        schema["properties"]["attributes"]["properties"]["statusCode"] = {
            "type": "integer",
            "description": "HTTP status code of the API response.",
            "minimum": 100,
            "maximum": 599
        }
        schema["properties"]["attributes"]["required"] = ["statusCode"]
    
    return schema

def generate_output_schema_files(base_dir, is_rest_api_connector):
    """
    Traverse the connector project and create output schema files for each operation.
    """
    ui_schema_dir = os.path.join(base_dir, "src", "main", "resources", "uischema")
    output_schema_dir = os.path.join(base_dir, "src", "main", "resources", "outputschema")
    
    # Ensure the output schema directory exists
    os.makedirs(output_schema_dir, exist_ok=True)
    
    # Loop through all files in the uischema directory
    for file_name in os.listdir(ui_schema_dir):
        if file_name.endswith(".json"):
            operation_name = os.path.splitext(file_name)[0]
            output_schema_file = os.path.join(output_schema_dir, f"{operation_name}.json")
            
            # Generate the output schema
            schema = create_output_schema(is_rest_api_connector, operation_name)
            
            # Write the schema to the file
            with open(output_schema_file, "w") as f:
                json.dump(schema, f, indent=2)
            
            print(f"Generated output schema for operation: {operation_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate output schema files for connector operations.")
    parser.add_argument("base_dir", help="Base directory of the connector project.")
    parser.add_argument("--rest-api", action="store_true", help="Specify if the connector is REST API-based.")
    args = parser.parse_args()
    
    generate_output_schema_files(args.base_dir, args.rest_api)
