from abc import ABC, abstractmethod
from typing import Iterable

class IChatWidget(ABC):

    def __init__(self, frame) -> None:
        self.frame = frame

    @abstractmethod
    def create_widgets(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_widgets(self) -> Iterable:
        raise NotImplemented()