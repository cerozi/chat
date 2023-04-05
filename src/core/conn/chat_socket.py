import socket

class ChatSocket(socket.socket):

    ENCODING = "ascii"

    def send(self, __data: str, *args) -> int:

        if not isinstance(__data, bytes):
            __data = __data.encode(self.ENCODING)

        return super().send(__data, *args)

    def sendall(self, __data: str, *args) -> None:
        
        if not isinstance(__data, bytes):
            __data = __data.encode(self.ENCODING)

        return super().sendall(__data, *args)