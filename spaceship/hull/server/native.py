from spaceship.hull.server.base import BaseServer


class NativeServer(BaseServer):
    def run_server(self) -> None:
        print(f"Running from {self.__class__.__name__}")
