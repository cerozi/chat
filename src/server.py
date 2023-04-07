from core.conn.controllers.server import ChatServer

with ChatServer(('127.0.0.1', 6666)) as server:
    
    server.start()