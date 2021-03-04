from abc import ABC, abstractmethod


class BaseServer(ABC):
    @abstractmethod
    def run_server(self) -> None:
        pass
