import os

def check_and_create_dir(path):
    if os.path.isdir(path):
        if os.path.exists(path) == False:
            os.makedirs(path)
    elif os.path.isfile(path):
        if os.path.exists(os.path.dirname(path)) == False:
            os.makedirs(path)