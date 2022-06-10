from multiprocessing import connection
import socket
import json
import threading
import time
from _thread import *
from prometheus_client import start_http_server, Gauge
# create server
print_lock = threading.Lock()
cpu=Gauge('cpu', 'cpu percent ')
ram=Gauge('ram', 'ram percent')
disk=Gauge('disk', 'disk percent')
ram_total=Gauge('ram_total', 'ram total')
ram_available=Gauge('ram_available', 'ram available')
ram_used=Gauge('ram_used', 'ram used')
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
def json_parser(datas):
    return json.loads(datas)

def accpet_client_data(connection):
    while True:
        data = recv_data(connection)
        data = json_parser(data)
        ram.set(data['ram'])
        cpu.set(data['cpu'])
        disk.set(data['disk'])
        ram_total.set(data['ram_total'])
        ram_available.set(data['ram_available'])
        ram_used.set(data['ram_used'])
        time.sleep(10)
        
    connection.close()    
    return data
#main
if __name__== '__main__':
    print("server started at port 45678")
    server=create_server('0.0.0.0',45678)
    start_http_server(1234)
    while True:
        connection,address=accept_client(server)
        print_lock.acquire()
        start_new_thread(accpet_client_data, (connection,))

