from core.conn.controllers.client import ChatClient

with ChatClient(('127.0.0.1', 6666)) as client:

    client.connect()
    client.start_communication()