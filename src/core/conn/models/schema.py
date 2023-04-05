import socket

class Client:

    def __init__(self, socket: socket.socket, nickname: str = None) -> None:
        self.socket = socket
        self.nickname = nickname

    def has_nickname(self) -> bool:
        return bool(self.nickname)

    def set_nickname(self, nick: str) -> None:
        self.nickname = nick