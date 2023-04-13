from core.conn.controllers.server import ServerConnection

with ServerConnection(('127.0.0.1', 6666)) as server:
    
    server.start()