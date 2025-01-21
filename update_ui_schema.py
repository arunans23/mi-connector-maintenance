import os
import json

# Define the response section to be added
RESPONSE_SECTION = {
    "type": "attributeGroup",
    "value": {
        "groupName": "Output",
        "elements": [
            {
                "type": "attribute",
                "value": {
                    "name": "responseVariable",
                    "displayName": "Output Variable Name",
                    "inputType": "string",
                    "deriveResponseVariable": true,
                    "required": "true",
                    "helpTip": "Name of the variable to which the output of the operation should be assigned"
                }
            },
            {
                "type": "attribute",
                "value": {
                    "name": "overwriteBody",
                    "displayName": "Overwrite Message Body",
                    "inputType": "checkbox",
                    "defaultValue": "true",
                    "helpTip": "Replace the Message Body in Message Context with the output of the operation (This will remove the payload from the above variable).",
                    "required": "false"
                }
            }
        ]
    }
}

def schema_contains_field(schema, field_name):
    """
    Check if the schema contains a field with the specified name.
    """
    for element in schema.get("elements", []):
        if element["type"] == "attribute" and element["value"].get("name") == field_name:
            return True
        if element["type"] == "attributeGroup":
            if schema_contains_field(element["value"], field_name):
                return True
    return False

def add_response_section_to_schema(file_path):
    """
    Add the response section to the UI schema if conditions are met.
    """
    with open(file_path, "r") as f:
        schema = json.load(f)
    print(f"Processing UI schema: {file_path}")
    
    # Check if the "Response" group already exists or "connectionName" is present
    if schema_contains_field(schema, "connectionName"):
        print(f"Schema contains 'connectionName'. Skipping update for {file_path}.")
        return
    
    if any(
        group["value"]["groupName"] == "Response"
        for group in schema.get("elements", [])
    ):
        print(f"Response section already exists in {file_path}. Skipping.")
        return

    # Append the Response section
    schema["elements"].append(RESPONSE_SECTION)

    # Write the updated schema back to the file
    with open(file_path, "w") as f:
        json.dump(schema, f, indent=2)
    
    print(f"Updated UI schema: {file_path}")

def update_ui_schemas(base_dir):
    """
    Traverse the connector's uischema directory and update each schema.
    """
    ui_schema_dir = os.path.join(base_dir, "src", "main", "resources", "uischema")

    if not os.path.exists(ui_schema_dir):
        print(f"UI schema directory does not exist: {ui_schema_dir}")
        return

    for file_name in os.listdir(ui_schema_dir):
        if file_name.endswith(".json"):
            file_path = os.path.join(ui_schema_dir, file_name)
            add_response_section_to_schema(file_path)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Update UI schemas with Response section.")
    parser.add_argument("base_dir", help="Base directory of the connector project.")
    args = parser.parse_args()

    update_ui_schemas(args.base_dir)
