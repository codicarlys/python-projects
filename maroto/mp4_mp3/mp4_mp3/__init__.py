__version__ = '0.1.0'

from moviepy.editor import *

videofile = VideoFileClip("input mp4 filename")
audiofile = videofile.audio
audiofile.write_audiofile("output mp3 filename")

videofile.close()
audiofile.close()