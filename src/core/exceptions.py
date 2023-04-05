class ClientNotConnectedError(BaseException):

    def __init__(self) -> None:
        msg = """The client socket is not connected to the server. To 
        start communication, call connect() first. """
        super().__init__(msg)