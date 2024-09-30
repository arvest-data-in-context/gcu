from .utils import get_text_file_properties
from moviepy.editor import VideoFileClip

def read_video(path):
    """Return video file as a numpy array."""

    return None

def write_video(file_object):
    """Write the contents of the File object as video."""

    pass

def get_video_properties(file_object):
    """Update the file_properties property with the file's properties."""
    props = get_text_file_properties(file_object)

    video = VideoFileClip(file_object.path)
    props["video_duration_ms"] = video.duration / 1000
    width, height = video.size
    props["width"] = width
    props["height"] = height
    props["video_frames"] = video.reader.nframes
    props["video_frame_rate"] = video.fps
    props["video_codec"] = video.reader.codec

    props["audio_duration_ms"] = video.audio.duration / 1000
    props["audio_channels"] = video.audio.nchannels
    props["audio_frame_rate"] = video.audio.fps
    props["audio_sample_width"] = video.audio.nbytes // video.audio.nchannels 
    props["audio_frames"] = video.audio.reader.nframes

    video.close()

    file_object.file_properties = props
    return props