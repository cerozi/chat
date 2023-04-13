import customtkinter

from core.conn.controllers.client import ClientConnection
from core.gui.app import ChatGUI

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = ChatGUI(ClientConnection(("127.0.0.1", 6666)))
app.mainloop()