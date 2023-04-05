import socket
import threading

from typing import Tuple

from core.exceptions import ClientNotConnectedError
from core.conn.chat_socket import ChatSocket

class ChatClient:

    def __init__(self, server_addr: Tuple[str, int]) -> None:

        self.__socket = None
        self.__connected = False
        self.__server_addr = server_addr

    def is_connected(self) -> bool:
        return self.__connected

    def __set_connected(self, connected: bool) -> None:
        self.__connected = connected
    
    def __write(self) -> None:

        nickname = input("Nickname: ")
        self.__socket.sendall(nickname)
        
        while (True):
            data = input()
            self.__socket.sendall(data)

    def __read(self) -> None:
        
        while (True):
            data = self.__socket.recv(1024)
            print(data.decode(ChatSocket.ENCODING))

    def connect(self) -> None:
        
        if self.__socket is None:
            self.__socket = ChatSocket(socket.AF_INET, socket.SOCK_STREAM)

        self.__socket.connect(self.__server_addr)
        self.__set_connected(True)

    def start_communication(self) -> None:

        if not self.is_connected():
            ClientNotConnectedError()

        writing = threading.Thread(target = self.__write)
        reading = threading.Thread(target = self.__read)

        writing.start()
        reading.start()

        writing.join()
        reading.join()

    def __enter__(self) -> None:
        self.__socket = ChatSocket(socket.AF_INET, socket.SOCK_STREAM)
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.__socket.close()