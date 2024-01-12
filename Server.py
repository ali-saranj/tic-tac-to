import socket

socket_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 5555
socket_server.bind((ip_address, port))
socket_server.listen()

server_conection, _ = socket_server.accept()

if server_conection:
    print("SERVER CONNECTED TO Client")
    server_conection.send("CLIENT CONNECTED TO SERVER".encode('utf-8'))

    while True:
        print(f"Client: {server_conection.recv(1024).decode('utf-8')}")
        server_conection.send(input(": ").encode('utf-8'))