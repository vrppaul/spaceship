import logging
import os
import sys
from typing import Optional

from spaceship.hull.hull import Hull
from spaceship.hull.server.util import KNOWN_SERVERS

DEFAULT_SETTINGS_FILENAME = "config.yaml"


def get_config_file_path(path: Optional[str], logger: logging.Logger) -> str:
    if not path:
        path = os.path.join(os.path.abspath(os.getcwd()), DEFAULT_SETTINGS_FILENAME)
        logger.info("No config path was provided. Trying default %s.", path)
    if os.path.isdir(path):
        logger.error("Specified path %s is a folder. You must provide a path to a config file.", path)
        sys.exit(1)
    if not os.path.exists(path):
        logger.error("No configuration file was found at given path %s.", path)
        sys.exit(1)
    return path


def set_hull_with_config(config_file_path: str, logger: logging.Logger) -> None:
    hull = Hull()
    hull.config.from_yaml(config_file_path)

    server_name = hull.config.server.name()
    if server_name not in KNOWN_SERVERS:
        logger.error("Provided server name `%s` is not in the list of known servers %s", server_name, KNOWN_SERVERS)
        sys.exit(1)

    hull.wire(modules=[sys.modules[sys.modules[__name__].__package__]])
