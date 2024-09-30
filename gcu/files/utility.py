# User-facing utility functions

import os

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