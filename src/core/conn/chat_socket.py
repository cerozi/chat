import socket
from datetime import datetime
from colorama import Fore

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

    def accept(self) -> tuple:
        
        __socket, __address =  super().accept()
        print(Fore.GREEN + f"[{datetime.now().strftime('%Y/%m/%d, %H:%m:%s')}] {__address[0]} joined the chat!")

        return __socket, __address

    def listen(self, *args) -> None:
        
        super().listen(*args)
        
        print()
        print(Fore.GREEN + "[STARTING] SERVER READY FOR CONNECTIONS!" + "\n")
