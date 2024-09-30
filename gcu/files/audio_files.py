from .utils import get_text_file_properties
from pydub import AudioSegment

def read_audio(path):
    """Return audio file as a numpy array."""

    return None

def write_audio(file_object):
    """Write the contents of the File object as audio."""

    pass

def get_audio_properties(file_object):
    """Update the file_properties property with the file's properties."""
    props = get_text_file_properties(file_object)

    audio = AudioSegment.from_file(file_object.path)
    props["duration_ms"] = len(audio)
    props["channels"] = audio.channels
    props["frame_rate"] = audio.frame_rate
    props["sample_width"] = audio.sample_width
    props["frames"] = audio.frame_count() 

    file_object.file_properties = props
    return props