from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name              = 'BradSmalley_Video_Looper',
      version           = '1.0.0',
      author            = 'Brad Smalley',
      author_email      = 'brad.smalley@gmail.com',
      description       = 'Application to turn your Raspberry Pi into a dedicated looping video playback device, good for art installations, information displays, or just playing cat videos all day.  Derived from the BradSmalley_Video_Looper available at https://github.com/adafruit/pi_video_looper.git',
      license           = 'GNU GPLv2',
      url               = 'https://github.com/BradSmalley/pi_video_looper',
      install_requires  = ['pyudev'],
      packages          = find_packages())
