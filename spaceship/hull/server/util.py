import logging
import sys

from dependency_injector.wiring import inject, Provide

from spaceship.hull import Hull, KNOWN_SERVERS
from spaceship.hull.server.base import BaseServer


@inject
def get_server(server: BaseServer = Provide[Hull.server]) -> BaseServer:
    return server


def set_hull_with_config(config_file_path: str, logger: logging.Logger) -> None:
    hull = Hull()
    hull.config.from_yaml(config_file_path)

    server_name = hull.config.server.server_name()
    if server_name not in KNOWN_SERVERS:
        logger.error("Provided server name `%s` is not in the list of known servers %s", server_name, KNOWN_SERVERS)
        sys.exit(1)

    hull.wire(modules=[sys.modules[__name__]])
