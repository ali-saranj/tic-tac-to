import socket
from TicTacTO import *

ticTacTO = TicTacTO()
socket_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 5358

socket_client.connect((ip_address, port))

data_receive = socket_client.recv(1024)

if data_receive:
    print(data_receive.decode('utf-8'))
    ticTacTO.showMap()

    while True:
        index = input(":")
        ticTacTO.setOandX(index, "O")
        ticTacTO.showMap()
        socket_client.send(index.encode('utf-8'))
        if ticTacTO.winner() != "z":
            print(f"{ticTacTO.winner()} is winner")
            break
        index = socket_client.recv(1024).decode('utf-8')
        ticTacTO.setOandX(index, "x")
        if ticTacTO.winner() != "z":
            print(f"{ticTacTO.winner()} is winner")
            break
        ticTacTO.showMap()
