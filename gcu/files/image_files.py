from .utils import get_text_file_properties
from PIL import Image

def read_image(path, **kwargs):
    """Return image file as a numpy array."""

    print(kwargs.get("hello", None))

    return None

def write_image(file_object):
    """Write the contents of the File object as image."""

    pass

def get_image_properties(file_object):
    """Update the file_properties property with the file's properties."""
    props = get_text_file_properties(file_object)

    with Image.open(file_object.path) as img:
        width, height = img.size
        props["width"] = width
        props["height"] = height
        props["color_mode"] = img.mode
        props["bit_depth"] = img.bits

    file_object.file_properties = props
    return props