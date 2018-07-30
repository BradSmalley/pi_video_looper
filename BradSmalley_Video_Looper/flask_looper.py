from flask import Flask
from flask import render_template
from video_looper2 import VideoLooper

from configparser import *

import importlib
import os
import re
import sys
import signal
import time
import subprocess
import pygame

from model import Playlist

config_path = '/boot/video_looper.ini'

app = Flask(__name__)
looper = VideoLooper(config_path)

@app.route('/hello/')
@app.route('/hello/<name>/')
def root(name=None):
    looper.run()
    return render_template('hello.html', name=name)

