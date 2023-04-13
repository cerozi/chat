import customtkinter

from core.gui.frames.interface.base_frame import IBaseFrame

class LoginFrame(IBaseFrame):

    def init_widgets(self) -> None:

        self.label = customtkinter.CTkLabel(master = self, text = "Nickname")
        self.entry = customtkinter.CTkEntry(master = self, placeholder_text = "Enter your nickname")
        self.button = customtkinter.CTkButton(master = self, text = "Join", width = 70)

        self.label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.entry.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.button.grid(row = 2, column = 0, padx = 10, pady = 10)
