from dependency_injector import containers, providers

from spaceship.hull.server.gunicorn_wrapper import GunicornWrapper
from spaceship.hull.server.native import NativeServer


class Hull(containers.DeclarativeContainer):

    config = providers.Configuration()

    server = providers.Selector(
        config.server.name,
        native=providers.Singleton(NativeServer),
        gunicorn=providers.Singleton(GunicornWrapper)
    )
