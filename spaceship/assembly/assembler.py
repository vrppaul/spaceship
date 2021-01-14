import argparse
import logging
import sys
import subprocess
from typing import Dict

import yaml

from spaceship.hull import DEFAULT_SETTINGS_FILENAME, get_config_file_path

COMPONENTS = ("server",)


def _install_packages_from_config(config_data: Dict[str, str], logger: logging.Logger):
    logger.info("Installing packages from the config.")
    for component in COMPONENTS:
        name = config_data.get(component, {}).get("name")
        if name is not None and name != "native":
            logger.info("Installing package %s", name)
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])
            except subprocess.CalledProcessError:
                logger.error("Installing packages from the config failed. Check the package names.")
                sys.exit(1)


def assemble(*, parser: argparse.ArgumentParser, logger: logging.Logger) -> None:
    parser.add_argument("--config_path", nargs="?", type=str,
                        help="Path to a file with project configs. "
                             f"Default is a file called {DEFAULT_SETTINGS_FILENAME} inside a cwd ('%(default)s')")
    args = parser.parse_args(sys.argv[2:])

    path = args.config_path
    config_file_path = get_config_file_path(path, logger)

    with open(config_file_path, "r") as stream:
        config_data = yaml.safe_load(stream)
        _install_packages_from_config(config_data, logger)
