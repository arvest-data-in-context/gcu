import os
import time

def check_and_create_dir(path):
    if os.path.isdir(path):
        if os.path.exists(path) == False:
            os.makedirs(path)
    elif os.path.isfile(path):
        if os.path.exists(os.path.dirname(path)) == False:
            os.makedirs(path)

def get_text_file_properties(file_object):
    """Update the file_properties property with the file's properties."""
    props = {}

    stats = os.stat(file_object.path)
    props["creation_time"] = time.ctime(stats.st_ctime)
    props["modified_time"] = time.ctime(stats.st_mtime)
    props["access_time"] = time.ctime(stats.st_atime)
    props["size"] = stats.st_size
    props["mode"] = stats.st_mode
    props["inode"] = stats.st_ino
    props["device_id"] = stats.st_dev
    props["hard_links"] = stats.st_nlink

    file_object.file_properties = props
    return props