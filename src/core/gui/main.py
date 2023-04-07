import customtkinter
from infra.frames.chat_frame import ChatFrame

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

class ChatGUI(customtkinter.CTk):

    WIDTH = 350
    HEIGHT = 350

    def __init__(self, *args, **kwargs) -> None:
        
        super().__init__(*args, **kwargs)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.chat_frame = ChatFrame(self)

chat = ChatGUI()
chat.mainloop()