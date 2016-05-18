# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import WatchedFileHandler

"""
  for auto rotate file when mignight, multiprocess not safe.
"""
def set_logger(filename):
    log = logging.getLogger()
    fmt_str = '[%(levelname)s %(asctime)s %(name)s @ %(process)d (%(filename)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt_str)
    fileTimeHandler = TimedRotatingFileHandler(filename, "MIDNIGHT", 1, 20)
    fileTimeHandler.setFormatter(formatter)
    log.addHandler(fileTimeHandler)
    log.setLevel(logging.DEBUG)
    return log

"""
 for one file to multiprocess, when you want to rotate file, you must mv file use contrab
 WatchedFileHandler will auto create new file
"""
def set_watch_logger(filename):
    log = logging.getLogger()
    fmt_str = '[%(levelname)s %(asctime)s %(name)s @ %(process)d (%(pathname)s/%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt_str)
    fileTimeHandler = WatchedFileHandler(filename)
    fileTimeHandler.setFormatter(formatter)
    log.addHandler(fileTimeHandler)
    log.setLevel(logging.DEBUG)
    return log
