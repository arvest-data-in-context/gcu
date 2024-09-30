import zipfile
import os

def download_colabs_folder_as_zip(path):
    """Download a folder from your google drive as a zip file."""

    temp_zip = os.path.basename(path) + ".zip"
    with zipfile.ZipFile(temp_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(path):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), path))

    files.download(temp_zip)
    os.remove(temp_zip)