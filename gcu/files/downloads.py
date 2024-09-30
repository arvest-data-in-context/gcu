import os
from .file import File
from typing import Union, List
import requests
import zipfile
from .utils import _process_media_get

def download(url, path = "", **kwargs) -> Union[File, List[File]]:
    """
    Download media at the given url to the given path in the current colab session.
    
    Default path is "content/". If the path doesn't exist, the path will be created. Will return a gcu.files.File object, or a list of gcu.file.File objects if multiple files were uploaded. If the upload is cancelled, returns None.

    url can be a list of urls.

    kwargs
    ----------
    new_filename (str)
        default: None. When None, the original file keeps it's name. When "_uuid", the filename is updated with a unique name. When any other string, the filename is updated (for multiple files, and incremental number is added).
    range (int)
        default: None
    read_content (bool)
        default: False. Will run the read_content() function on the File objects once the file is retrieved.
    read_kwargs (dict)
        default: {}. The kwargs that are passed to the read_content() function.
    """

    downloaded = []
    if isinstance(url, str):
        url = [url]
    for item in url:
        _download_online_file(item, os.path.join("/content", os.path.basename(item)), kwargs.get("range", None))
        downloaded.append(os.path.join(os.path.basename(item)))

    if len(downloaded) > 0:
        return _process_media_get(path, downloaded, kwargs.get("new_filename", None), read_content = kwargs.get("read_content", False), read_kwargs = kwargs.get("read_kwargs", {}))
    else:
        return None
    
def _download_online_file(url, path, range):
    """Download a file to base colab directory."""
    if range == None:
        response = requests.get(url, stream=True)
    else:
        response = requests.get(url, headers={'Range': f'bytes={range}'}, stream=True)
    if response.status_code == 206 or response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

def download_zip(url, path):
    """Download a zip file and unpack it's contents at the given path (a folder of the filename will be created)."""
    
    # Download file:
    response = requests.get(url)
    temp_zip = os.path.join(path, os.path.basename(url))
    with open(temp_zip, 'wb') as file:
        file.write(response.content)

    # Create the output folder:
    if os.path.isdir(path) == False:
        os.makedirs(path)

    # Unzip:
    with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
        zip_ref.extractall(path)
    
    # Remove temporary ip file:
    os.remove(temp_zip)