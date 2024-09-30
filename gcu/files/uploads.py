from .utils import _process_media_get
from .file import File
from typing import Union, List

# If working locally, create a mock google.colab package:
try:
    from google.colab import files
except ImportError:
    class MockColabFiles:
        @staticmethod
        def upload():
            print("Mock upload function called")
            return None

    files = MockColabFiles()

def upload(path = "", **kwargs) -> Union[File, List[File], None]:
    """
    Uploads files to the given path in the current colab session.
    
    Default path is "content/". If the path doesn't exist, the path will be created. Will return a gcu.files.File object, or a list of gcu.file.File objects if multiple files were uploaded. If the upload is cancelled, returns None.

    kwargs
    ----------
    new_filename (str)
        default: None. When None, the original file keeps it's name. When "_uuid", the filename is updated with a unique name. When any other string, the filename is updated (for multiple files, and incremental number is added).
    read_content (bool)
        default: False. Will run the read_content() function on the File objects once the file is retrieved.
    read_kwargs (dict)
        default: {}. The kwargs that are passed to the read_content() function.
    """

    # Trigger upload
    uploaded = files.upload()

    if uploaded:
        return _process_media_get(path, list(uploaded.keys()), kwargs.get("new_filename", None), read_content = kwargs.get("read_content", False), read_kwargs = kwargs.get("read_kwargs", {}))
    else:
        return None
