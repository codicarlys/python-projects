__version__ = '0.1.0'

from matplotlib.pyplot import bar
from progressbar import ProgressBar
import urllib.request

def Donwloading(count, size, total_size):
    global bar
    if bar is None:
        bar = ProgressBar(maxval=total_size)
        bar.start()
    
    download = count * size
    if download < total_size:
        bar.update(download)
    else:
        bar.finish()
        bar = None

global bar
bar = None
url="https://youtu.be/kjBOesZCoqc?list=PL0-GT3co4r2y2YErbmuJw2L5tW4Ew2O5B"
print("Downloading.....")
urllib.request.urlretrieve(url, "output.mp4", Donwloading)