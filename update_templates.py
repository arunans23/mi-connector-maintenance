import os
from lxml import etree

RESPONSE_PARAMETERS = [
    {"name": "responseVariable", "description": "The name of the variable to which the response should be stored."},
    {"name": "overwriteBody", "description": "Replace the Message Body in Message Context with the response of the operation."},
]

def add_parameters_to_template(file_path):
    try:
        parser = etree.XMLParser(remove_blank_text=False)
        tree = etree.parse(file_path, parser)
        root = tree.getroot()

        # Check if the parameters already exist
        existing_params = {param.get("name") for param in root.findall(".//{http://ws.apache.org/ns/synapse}parameter")}
        if any(param["name"] in existing_params for param in RESPONSE_PARAMETERS):
            print(f"Response parameters already exist in {file_path}. Skipping.")
            return

        # Add new parameters before the sequence element
        sequence_element = root.find(".//{http://ws.apache.org/ns/synapse}sequence")
        if sequence_element is None:
            print(f"No <sequence> element found in {file_path}. Skipping.")
            return

        # Insert parameters with proper indentation
        for param in RESPONSE_PARAMETERS:
            new_param = etree.Element(
                "parameter",
                name=param["name"],
                description=param["description"]
            )
            root.insert(root.index(sequence_element), new_param)

        # Add a newline after each parameter for readability
        for elem in root.iterchildren():
            elem.tail = "\n    "

        root[-1].tail = "\n"  # Ensure the last child has consistent spacing
        tree.write(file_path, pretty_print=True, xml_declaration=True, encoding="UTF-8")
        print(f"Updated operation template: {file_path}")

    except etree.XMLSyntaxError as e:
        print(f"Error parsing XML file {file_path}: {e}")

def update_operation_templates(base_dir):
    resources_dir = os.path.join(base_dir, "src", "main", "resources")
    if not os.path.exists(resources_dir):
        print(f"Resources directory does not exist: {resources_dir}")
        return

    for root, _, files in os.walk(resources_dir):
        for file_name in files:
            if file_name.endswith(".xml") and file_name not in ["component.xml", "connector.xml", "init.xml"]:
                file_path = os.path.join(root, file_name)
                add_parameters_to_template(file_path)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Update operation templates with response parameters.")
    parser.add_argument("base_dir", help="Base directory of the connector project.")
    args = parser.parse_args()

    update_operation_templates(args.base_dir)
