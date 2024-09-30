import json
import xml.etree.ElementTree as ET
import os

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

    with open(os.path.join(file_object.path, file_object.filename), 'w') as json_file:
        json.dump(file_object.content, json_file, indent=kwargs.get("indent", 2))

def write_xml(file_object):
    """Write the contents of the File object as xml."""

    pass