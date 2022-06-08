from multiprocessing import connection
import socket
import json
import threading
from _thread import *
# create server
print_lock = threading.Lock()
def create_server(ip,port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip,port))
    s.listen()
    return s    
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
    return connection,address
#read json
def json_parser(json):
    return json.loads(json)

def accpet_client_data(connection):
    while True:
        data = recv_data(connection)
        
        data = json_parser(data)
    connection.close()    
    return data
#main
if __name__== '__main__':
    server=create_server('0.0.0.0',8080)
    while True:
        connection,address=accept_client(server)
        print_lock.acquire()
        start_new_thread(accpet_client_data, (connection,))

