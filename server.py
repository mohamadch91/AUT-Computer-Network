import socket

# create server
def create_server(ip,port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip,port))
    s.listen()    
# send data to client
def send_data(connection,json):
    connection.send(json.encode())
# receive data from client
def recv_data(connection):
    return connection.recv(2048).decode()

#accept client connection
def accept_client(s):
    connection, address = s.accept()
    print('Connection from: ' + str(address))
    return connection


