import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 25565        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #data = s.recv(1024)
    #s.sendall(b'Hello, world')
    try:
        s.sendall(b"Hello world")
        response = s.recv(1024)       
    finally:
        s.close()
    

print('Received:', response.decode('utf-8'))