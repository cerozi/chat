import customtkinter

from src.core.gui.frames.chat import ChatFrame
from src.core.gui.frames.login import LoginFrame

class ChatGUI(customtkinter.CTk):

    WIDTH = 400
    HEIGHT = 400

    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)

        self.title("Desktop Chat App")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)

        self.login = LoginFrame(self)
        self.chat = ChatFrame(self)

        self.display_frame(self.login)
        self.login.button.configure(command = lambda: self.switch_frames(self.chat, self.login))

    def display_frame(self, frame: customtkinter.CTkFrame) -> None:
        
        frame.init_widgets()
        frame.pack(expand = True)

    def switch_frames(self, new_frame: customtkinter.CTkFrame, old_frame: customtkinter.CTkFrame) -> None:
        
        old_frame.pack_forget()
        self.display_frame(new_frame)
