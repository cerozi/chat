import customtkinter
import threading

from core.conn.controllers.client import ClientConnection

from core.gui.frames.chat import ChatFrame
from core.gui.frames.login import LoginFrame

from core.gui.frames.interface.base_frame import IBaseFrame

class ChatGUI(customtkinter.CTk):

    WIDTH = 400
    HEIGHT = 400

    def __init__(self, conn: ClientConnection, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)

        self.__conn = conn
        self.__conn.connect()

        assert self.__conn.is_connected() is True

        self.title("Desktop Chat App")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)

        self.login = LoginFrame(self)
        self.chat = ChatFrame(self)

        self.display_frame(self.login)
        self.login.button.configure(command = self.__auth)

    def __auth(self) -> None:

        nickname = self.login.entry.get()
        if not nickname:
            return -1

        self.switch_frames(self.chat, self.login)
        self.chat.button.configure(command = self.__write)

        self.__start_communication(entry_data = nickname)

    def __write(self) -> None:

        data = self.chat.entry.get()
        if not data:
            return -1

        self.__conn.send(data)

    def __start_communication(self, entry_data: str = None) -> None:

        if hasattr(self, "reading"):
            return -1

        self.reading = threading.Thread(target = self.__display_messages, daemon = True)
        self.reading.start()

        if bool(entry_data):
            self.__conn.send(entry_data)

    def __display_messages(self) -> None:

        while (True):

            data = self.__conn.recv()

            self.chat.messages.configure(state = customtkinter.NORMAL)
            self.chat.messages.insert(customtkinter.END, data + "\n")
            self.chat.messages.configure(state = customtkinter.DISABLED)

            self.chat.entry.delete(0, customtkinter.END)

    def display_frame(self, frame: IBaseFrame) -> None:
        
        frame.init_widgets()
        frame.pack(expand = True)

    def switch_frames(self, new_frame: IBaseFrame, old_frame: IBaseFrame) -> None:
        
        old_frame.pack_forget()
        self.display_frame(new_frame)
