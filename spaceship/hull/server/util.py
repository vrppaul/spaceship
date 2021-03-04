from dependency_injector.wiring import inject, Provide

from spaceship.hull import Hull
from spaceship.hull.server.base import BaseServer

KNOWN_SERVERS = ("native", "gunicorn")


@inject
def get_server(server: BaseServer = Provide[Hull.server]) -> BaseServer:
    return server
