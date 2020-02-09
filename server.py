import socket

HOST = '127.0.0.1'
PORT = 9500
welcomeMsg = 'Hi'
partingMsg = 'GoodBye'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.bind((HOST, PORT))
    s.listen()
    print(f"listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    with conn: 
        print(f"Incoming connection from {addr}") 
        while True: 
            data = conn.recv(9500)
            if not data: 
                break 

            if data == b'Hello':
                conn.send(bytes(welcomeMsg, "utf-8"))

            else:
                conn.send(bytes(partingMsg, "utf-8"))

