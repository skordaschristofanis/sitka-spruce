"""
Handling loggers
"""


import logging
from logging.handlers import RotatingFileHandler
from platformdirs import user_log_path
from pathlib import Path

LOGDIR = user_log_path('sitka_spruce',
                       appauthor=False,
                       ensure_exists=True)

# set up default logging configureation
_FORMAT = "[%(asctime)s | %(name)-s | %(levelname)-8s] %(message)s"
_DATEFMT = "%Y-%m-%d %H:%M:%S"

_LEVELS = {"DEBUG": logging.DEBUG,
           "INFO": logging.INFO,
           "WARNING": logging.WARNING,
           "ERROR": logging.ERROR,
           "FATAL": logging.FATAL,
           "CRITICAL": logging.CRITICAL}


LOGINIT = False

def get_logger(name='sitka', level="INFO"):
    """Utility function to get the logger with customization

    .. warning:: NOT WORKING AS EXPECTED -> FIXME!!!

    Parameters
    ----------
    name : str        name of the logger
    level : str (optional)   logging level ['INFO']
    """
    logfile = LOGDIR / f'{name}.log'
    handler = RotatingFileHandler(logfile, mode='a',
                                  maxBytes=5.0e5, backupCount=5)

    handler.setFormatter(logging.Formatter(_FORMAT, _DATEFMT))
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(_LEVELS[level])
    return logger
