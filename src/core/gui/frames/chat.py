import customtkinter

class ChatFrame(customtkinter.CTkFrame):
    
    def __init__(self, master, *args, **kwargs) -> None:
        
        super().__init__(master, *args, **kwargs)
        self.master = master

    def init_widgets(self) -> None:

        self.scrollbar = customtkinter.CTkScrollbar(master = self)

        self.messages = customtkinter.CTkTextbox(master = self, state = customtkinter.DISABLED, width = 370, height = 340, yscrollcommand = self.scrollbar.set)
        self.entry = customtkinter.CTkEntry(master = self, width = 320)
        self.button = customtkinter.CTkButton(master = self, width = 20, text = "Send")
        
        self.messages.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)
        self.entry.grid(row = 1, column = 0)
        self.button.grid(row = 1, column = 1)
