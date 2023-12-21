import socket

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.connect(('127.0.0.1', 8888))
    mess - server.send("Hello")
    
