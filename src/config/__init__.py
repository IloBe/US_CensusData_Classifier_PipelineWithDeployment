# a user can manipulate configuration from project libraries like any other Python object

import logging
from logging import Formatter, NullHandler
from colorama import Fore, Style
from src.config.config import get_config, get_data_path, get_models_path, get_project_root_path


print(f'Invoking __init__.py for {__name__}')

COLORS = {"DEBUG": Fore.BLUE,
          "INFO": Fore.BLACK,
          "WARNING": Fore.YELLOW,
          "ERROR": Fore.RED,
          "CRITICAL": Fore.MAGENTA}


class CustomColoredFormatter(Formatter):
    def __init__(self, *, format, use_color):
        ''' Initialise customized formatter class '''
        Formatter.__init__(self, fmt=format)
        self.use_color = use_color

    def format(self, record):
        ''' Sets message colour according log level '''
        msg = super().format(record)
        if self.use_color:
            levelname = record.levelname
            if hasattr(record, "color"):
                return f"{record.color}{msg}{Style.RESET_ALL}"
            if levelname in COLORS:
                return f"{COLORS[levelname]}{msg}{Style.RESET_ALL}"
        return msg


logging.getLogger(__name__).addHandler(NullHandler())
config_dict = {}
