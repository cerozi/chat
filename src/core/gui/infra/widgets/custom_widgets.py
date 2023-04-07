import customtkinter

from infra.widgets.interfaces.interface import IChatWidget

class LoginWidgets(IChatWidget):

    def create_widgets(self) -> None:

        self.label = customtkinter.CTkLabel(master = self.frame, text = "Nickname")
        self.entry = customtkinter.CTkEntry(master = self.frame, placeholder_text = "Qual seu nickname?")
        self.button = customtkinter.CTkButton(master = self.frame, text = "Entrar")

        self.label.place(relx = 0.5, rely = 0.35, anchor="center")
        self.entry.place(relx = 0.5, rely = 0.5, anchor="center")
        self.button.place(relx = 0.5, rely = 0.65, anchor="center")

    def get_widgets(self) -> None:

        return [self.label, self.entry, self.button]

class ChatWidgets(IChatWidget):

    def create_widgets(self) -> None:

        self.entry = customtkinter.CTkEntry(master = self.frame, width = 250)
        self.button = customtkinter.CTkButton(master = self.frame, text = "Enviar", width = 50)

        self.entry.place(relx = 0.01, rely = 0.9)
        self.button.place(relx = 0.8, rely = 0.9)

    def get_widgets(self) -> None:

        return [self.entry, self.button]