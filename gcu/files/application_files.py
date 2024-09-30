import json
import xml.etree.ElementTree as ET

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

    pass

def write_xml(file_object):
    """Write the contents of the File object as xml."""

    pass