import os
import mimetypes
from .text_files import *
from .application_files import *
from .video_files import *
from .audio_files import *
from .image_files import *

class File:
    def __init__(self, **kwargs) -> None:
        """
        An object representing any kind of file.

        properties
        ----------
        path (str)
            path in the google colabs content/ folder
        filename (str)
            just the filename as a string including extension
        dir (str)
            just the folder path as a string
        ext (str)
            file extension
        mime (list)
            the file's mime type (found using mimetypes.guess_type())
        content ()
            the content of the file. This will vary according to file type.

        kwargs
        ----------
        read_content (bool)
            default: False. Run the read_content() function on creation.
        read_kwargs (dict)
            default: {}. The kwargs that are passed to the read_content() function.

        methods
        ----------
        read_content()
            retrive the content of the file, the return type changes according to the type of file.
        """

        self.path = kwargs.get("path", None)
        self.filename = kwargs.get("filename", None)
        self.dir = kwargs.get("dir", None)
        self.ext = kwargs.get("ext", None)
        self.mime = kwargs.get("mime", None)

        # If path local given, get filename and directory:
        if self.path != None:
            self.filename = os.path.basename(self.path)
            self.dir = os.path.dirname(self.path)

        # If filename given, get extension and mime type:
        
        if self.filename != None:
            self.ext = os.path.splitext(self.filename)[1][1:]
            self.mime = mimetypes.guess_type(self.filename)[0].split("/")

        self.content = kwargs.get("content", None)

        if kwargs.get("read_content", True):
            if self.filename != None and self.content == None:
                self.read_content(**kwargs.get("read_kwargs", {}))

    def write(self, **kwargs):
        """Write the contents of the file at its folder under its filename."""

        if self.mime[0] == "image":
            write_image(self)
        elif self.mime[0] == "audio":
            write_audio(self)
        elif self.mime[0] == "video":
            write_video(self)
        elif self.mime[0] == "application":
            if self.mime[1] == "json":
                write_json(self, **kwargs)
            elif self.mime[1] == "xml":
                write_xml(self)
            else:
                self._cannot_write_data()
        elif self.mime[0] == "text":
            if self.mime[1] == "plain":
                write_plain(self)
            elif self.mime[1] == "csv":
                write_csv(self)
            else:
                self._cannot_write_data()
        else:
            self._cannot_write_data()

    def read_content(self, **kwargs):
        """
        Retrive the content of the file, the return type changes according to the type of file.
        """

        if self.mime[0] == "image":
            self.content = read_image(self.path, **kwargs)
        elif self.mime[0] == "audio":
            self.content = read_audio(self.path)
        elif self.mime[0] == "video":
            self.content = read_video(self.path)
        elif self.mime[0] == "application":
            if self.mime[1] == "json":
                self.content = read_json(self.path)
            elif self.mime[1] == "xml":
                self.content = read_xml(self.path)
            else:
                self.content = self._cannot_read_data()
        elif self.mime[0] == "text":
            if self.mime[1] == "plain":
                self.content = read_plain_text(self.path)
            elif self.mime[1] == "csv":
                self.content = read_csv(self.path, **kwargs)
            else:
                self.content = self._cannot_read_data()
        else:
            self.content = self._cannot_read_data()
        
    def _cannot_read_data(self):
        """Return none when cannot read content."""

        print("This file type is not supported for content retrieval!")
        return None
    
    def _cannot_write_data(self):
        """Feedback for being unable to write content."""

        print("This file type is not supported for content writing!")
        return None