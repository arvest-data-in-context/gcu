import os
import uuid
from .file import File

def check_and_create_dir(path):
    if os.path.isdir(path):
        if os.path.exists(path) == False:
            os.makedirs(path)
    elif os.path.isfile(path):
        if os.path.exists(os.path.dirname(path)) == False:
            os.makedirs(path)

def _process_media_get(path, file_list, new_filename, **kwargs):
    """Once a file has been retrived, move it and return File objects."""   

    # Create directory if needed
    if os.path.isdir(os.path.join("/content", path)) == False:
        os.makedirs(os.path.join("/content", path))

    # Create a list of new names if needed
    new_names = file_list

    # As uuids
    if new_filename == "_uuid":
        new_names = []
        for item in file_list:
            new_names.append(str(uuid.uuid4()) + os.path.splitext(os.path.basename(item))[1])
    
    # As string
    elif isinstance(new_filename, str):
        new_names = []
        if len(file_list) == 1:
            new_names.append(new_filename + os.path.splitext(os.path.basename(file_list[0]))[1])
        else:
            for i, item in enumerate(file_list):
                new_names.append(new_filename + f" {i}" + os.path.splitext(os.path.basename(item))[1])
    
    # Move uploaded files
    for i, item in enumerate(file_list):
        original_path = os.path.join('/content', item)
        new_path = os.path.join("/content", path, new_names[i])
        os.rename(original_path, new_path)

    # Create File objects
    path_to_add = os.path.join("/content", path)
    if path == "":
        path_to_add = "/content"
    if len(file_list) == 1:
        return File(path = os.path.join(path_to_add, new_names[0]), read_content = kwargs.get("read_content", False), read_kwargs = kwargs.get("read_kwargs", {}))
    else:
        ret = []
        for filename in new_names:
            ret.append(File(path = os.path.join(path_to_add, filename), read_content = kwargs.get("read_content", False), read_kwargs = kwargs.get("read_kwargs", {})))
        return ret
    
def collect_files(path, acceptedFormats = []):
    """Collect all files of accepted format in a given directory."""

    finalList = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if len(acceptedFormats) > 0:
                extension = os.path.splitext(file)[1][1:]
                if extension in acceptedFormats:
                    finalList.append(os.path.join(root, file))
            else:
                finalList.append(os.path.join(root, file))
    return finalList