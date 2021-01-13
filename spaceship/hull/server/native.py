from spaceship.hull.server.interface import ServerInterface


class NativeServer(ServerInterface):
    def run_server(self) -> None:
        print(f"Running from {self.__class__.__name__}")
