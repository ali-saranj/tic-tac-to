import socket

# creating socket instance
socket_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# target ip address and port
ip_address = '127.0.0.1'
port = 5555

# instance requesting for connection to the specified address and port
socket_client.connect((ip_address, port))

# receiving response from server
data_receive = socket_client.recv(1024)

# if response is not null
if data_receive:
    # Connection is successful
    print(data_receive.decode('utf-8'))

    while True:
        socket_client.send(input(":").encode('utf-8'))
        print(f"SERVER: {socket_client.recv(1024).decode('utf-8')}")
