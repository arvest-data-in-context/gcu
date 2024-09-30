import json
import xml.etree.ElementTree as ET
from .utils import check_and_create_dir

def read_json(path):
    """Return json file as dict."""

    with open(path, 'r') as f:
        return json.load(f)

def read_xml(path):
    """Return xml file as and xml.etree.ElementTree."""

    tree = ET.parse(path)
    root = tree.getroot()
    return root

def write_json(file_object, **kwargs):
    """Write the contents of the File object as json."""

    check_and_create_dir(file_object.dir)

    # This because prezi3 gives string format. 
    content = file_object.content
    if isinstance(file_object.content, str):
        content = json.loads(file_object.content)

    with open(file_object.path, 'w') as json_file:
        json.dump(content, json_file, indent=kwargs.get("indent", 2))

def write_xml(file_object):
    """Write the contents of the File object as xml."""

    pass