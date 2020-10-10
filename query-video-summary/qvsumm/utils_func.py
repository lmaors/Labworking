import os
from os.path import dirname, abspath

import numpy as np
# import urllib

from moviepy.editor import *

import scipy.misc
import shutil


def preprocess_video(query, videoURL,video_name):

    # Gquery = query
    # video = pafy.new(videoURL)
    # for s in video.streams:
    #     if s.resolution == '640x360':
    #         best = s
    # direc = '../../experiment/chapter_0/'
    direc = dirname(dirname(dirname(abspath(__file__)))) + '/experiment/chapter_0'

    # if not os.path.exists(direc):
    #     os.makedirs(direc)
    # filename = best.download(quiet=True, filepath=direc + "/" + Gquery[0:len(Gquery)] + ".mp4")
    # f = direc + "/" + Gquery[0:len(Gquery)] + ".mp4"
    f = direc +'/' + video_name
    clip = VideoFileClip(f)
    time = clip.duration
    imagenames = []
    for k, c in enumerate(np.arange(0.5, time, 1)):
        im = clip.get_frame(c)
        imagepath = direc + "/frames/"
        if os.path.exists(imagepath) and k == 0:
            shutil.rmtree(imagepath)
        if not os.path.exists(imagepath):
            os.makedirs(imagepath)
        imagepath = imagepath + str(k) + '.png'
        scipy.misc.imsave(imagepath, im)
        imagenames.append(imagepath)
    return imagenames


