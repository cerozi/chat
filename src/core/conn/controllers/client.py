import socket

from typing import Tuple

from core.conn.chat_socket import ChatSocket

class ClientConnection:

    def __init__(self, server_addr: Tuple[str, int]) -> None:

        self.__socket = None
        self.__connected = False
        self.__server_addr = server_addr

    def is_connected(self) -> bool:

        return self.__connected

    def __set_connected(self, connected: bool) -> None:

        self.__connected = connected
    
    def send(self, data: str | bytes) -> None:

        self.__socket.sendall(data)

    def recv(self) -> str:
        
        data = self.__socket.recv(1024)
        return data.decode(ChatSocket.ENCODING)

    def connect(self) -> None:
        
        if self.__socket is None:
            self.__socket = ChatSocket(socket.AF_INET, socket.SOCK_STREAM)

        self.__socket.connect(self.__server_addr)
        self.__set_connected(True)

    def __enter__(self) -> None:

        self.__socket = ChatSocket(socket.AF_INET, socket.SOCK_STREAM)
        return self

    def __exit__(self, *args, **kwargs) -> None:

        self.__socket.close()