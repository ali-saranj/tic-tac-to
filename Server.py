import socket
from TicTacTO import *

ticTacTO = TicTacTO()
socket_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 5358
socket_server.bind((ip_address, port))
socket_server.listen()

server_conection, _ = socket_server.accept()

if server_conection:
    print("SERVER CONNECTED TO Client")
    ticTacTO.showMap()
    server_conection.send("CLIENT CONNECTED TO SERVER".encode('utf-8'))

    while True:
        index = server_conection.recv(1024).decode('utf-8')
        ticTacTO.setOandX(index,"O")
        if ticTacTO.winner() != "z":
            print(f"{ticTacTO.winner()} is winner")
            break
        ticTacTO.showMap()
        index = input(": ")
        ticTacTO.setOandX(index, "x")
        ticTacTO.showMap()
        server_conection.send(index.encode('utf-8'))
        if ticTacTO.winner() != "z":
            print(f"{ticTacTO.winner()} is winner")
            break