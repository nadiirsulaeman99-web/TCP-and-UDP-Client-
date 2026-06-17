import socket


host = '127.0.0.1'
port = 9999

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
Socket.connect((host, port))

Socket.send("Hello TCP server...".encode('utf-8'))
print(Socket.recv(1024))