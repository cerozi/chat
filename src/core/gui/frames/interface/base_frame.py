from abc import ABC, abstractmethod
from customtkinter import CTkFrame

class IBaseFrame(CTkFrame, ABC):

    @abstractmethod
    def init_widgets(self) -> None:
        raise NotImplementedError()