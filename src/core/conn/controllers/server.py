import queue
import socket
import threading

from typing import Tuple

from core.conn.models.schema import Client
from core.conn.chat_socket import ChatSocket

class ChatServer:

    def __init__(self, addr: Tuple[str, int]) -> None:

        self.__addr = addr
        self.__socket = None
        self.__clients = list()
        self.__messages = queue.Queue()

    def __init_configs(self) -> None:

        if self.__socket is None:
            self.__socket = ChatSocket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.__socket.bind(self.__addr)
        self.__socket.listen()
        
        broadcasting = threading.Thread(target = self.__broadcast)
        broadcasting.start()

    def __accept_conn(self) -> None:

        while (True):

            socket, __ = self.__socket.accept()
            client = Client(socket)
            self.__clients.append(client)

            clienthandler = threading.Thread(target = self.__client_handler, args = (client, ))
            clienthandler.start()

    def __broadcast(self) -> None:

        while (True):
            
            msg = self.__messages.get()

            if not isinstance(msg, bytes):
                msg = msg.encode(ChatSocket.ENCODING)

            for client in self.__clients:
                client.socket.sendall(msg)

    def __client_handler(self, client: Client) -> None:
        
        while (True):

            data = client.socket.recv(1024)

            if not client.has_nickname():
                client.set_nickname(data.decode(ChatSocket.ENCODING))
                data = f"{client.nickname} entrou no chat!"

            if not data:
                self.__clients.remove(client)
                data = f"{client.nickname} saiu do chat!"

            self.__messages.put(data)

    def start(self) -> None:

        self.__init_configs()
        self.__accept_conn()
    
    def __enter__(self) -> None:
        self.__socket = ChatSocket(socket.AF_INET, socket.SOCK_STREAM)
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.__socket.close()