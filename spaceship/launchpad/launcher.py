import argparse
import logging
import os
import sys
import time
from typing import Optional

from spaceship.hull.server.util import get_server, set_hull_with_config


DEFAULT_SETTINGS_FILENAME = "config.yaml"


def _initiate_countdown(countdown: int, logger: logging.Logger) -> None:
    """
    Just a funny countdown, simulating real spaceship start
    """
    logger.info("Activate main engine hydrogen burnoff system")
    time.sleep(1)
    logger.info(f"Countdown before the start. Time T-{countdown} seconds.")
    for i in range(countdown, 0, -1):
        logger.info(i)
        time.sleep(1)
    logger.info("Main engine start")
    time.sleep(1)


def _get_config_file_path(path: Optional[str], logger: logging.Logger) -> str:
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


def launch(*, parser: argparse.ArgumentParser, logger: logging.Logger) -> None:
    parser.add_argument("--countdown", nargs="?", type=int, const=10,
                        help="Count before the start. Default count is %(const)s.")
    parser.add_argument("--config_path", nargs="?", type=str,
                        help="Path to a file with project configs. "
                             f"Default is a file called {DEFAULT_SETTINGS_FILENAME} inside a cwd ('%(default)s')")
    args = parser.parse_args(sys.argv[2:])

    path = args.config_path
    config_file_path = _get_config_file_path(path, logger)
    set_hull_with_config(config_file_path, logger)

    countdown = args.countdown
    if countdown:
        _initiate_countdown(countdown, logger)
    logger.info("Solid rocket booster ignition and liftoff!")

    # Get the server specified in the configuration and run it with the supported arguments
    get_server().run_server()
