import customtkinter

from src.core.gui.frames.chat import ChatFrame
from src.core.gui.frames.login import LoginFrame

from src.core.gui.frames.interface.base_frame import IBaseFrame

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

    def display_frame(self, frame: IBaseFrame) -> None:
        
        frame.init_widgets()
        frame.pack(expand = True)

    def switch_frames(self, new_frame: IBaseFrame, old_frame: IBaseFrame) -> None:
        
        old_frame.pack_forget()
        self.display_frame(new_frame)
