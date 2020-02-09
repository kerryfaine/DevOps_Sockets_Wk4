import socket

HOST = '127.0.0.1'
PORT = 9500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.connect((HOST, PORT))
    s.sendall(b'Hello')
    dataFromTry1 = s.recv(1024)

    s.sendall(b'Hello, Server!')
    dataFromTry2 = s.recv(1024)

print(f'Connection 1 Received:  {repr(dataFromTry1)}')
print(f'Connection 2 Received:  {repr(dataFromTry2)}')
