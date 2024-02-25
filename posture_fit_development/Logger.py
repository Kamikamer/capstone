from enum import Enum
import json
import logging
import logging.config
import logging.handlers
import pathlib

logger = logging.getLogger("PostureFIT")

class CustomLogger():
    def __init__(self, custom_config: bool):
        self.logger = logging.getLogger("PostureFIT")
        logger.setLevel(logging.DEBUG)
#        if custom_config:
#            config_file = pathlib.Path("../assets/config.json")
#            with open(config_file) as f_in:
#                config = json.load(f_in)
#            logging.config.dictConfig(config)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(CustomColors())
        logger.addHandler(ch)
        

class CustomColors(logging.Formatter):
    grey = "\x1b[38;20m"
    cyan = "\x1b[36;20m"
    blue = "\x1b[34;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(levelname)s -> %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: blue + format + reset,
        logging.INFO: cyan + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
