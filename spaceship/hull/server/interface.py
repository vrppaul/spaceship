from abc import ABC, abstractmethod


class ServerInterface(ABC):
    @abstractmethod
    def run_server(self) -> None:
        pass
