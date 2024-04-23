import xml.etree.ElementTree as ET

def check_gazebo_references(urdf_file):
    tree = ET.parse(urdf_file)
    root = tree.getroot()

    errors = []

    # Find all gazebo references
    gazebo_tags = root.findall(".//gazebo")
    for gazebo_tag in gazebo_tags:
        reference = gazebo_tag.get("reference")
        # Check if the reference meets your requirements
        if reference not in required_gazebo_references:
            errors.append(f"Invalid gazebo reference: {reference}")

    return errors

# Define your required gazebo references
required_gazebo_references = ["base_link", "other_link"]

# Path to your URDF file
urdf_file_path = "/opt/ros/noetic/share/urdf_tutorial/urdf/08-macroed.urdf.xacro"

# Check gazebo references
errors = check_gazebo_references(urdf_file_path)
if errors:
    print("Gazebo reference errors:")
    for error in errors:
        print(error)
else:
    print("All gazebo references are valid.")
