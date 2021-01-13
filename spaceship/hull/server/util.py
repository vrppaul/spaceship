from spaceship.hull.server.interface import ServerInterface
from spaceship.hull.server.native import NativeServer


def get_server() -> ServerInterface:
    return NativeServer()
