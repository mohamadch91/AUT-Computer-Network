from multiprocessing import connection
import socket
import json
import threading
import time
import random
from _thread import *
from prometheus_client import start_http_server, Gauge
# create server
# print_lock = threading.Lock()
cpu=Gauge('cpu', 'cpu percent ',["client_no"])
ram=Gauge('ram', 'ram percent',["client_no"])
disk=Gauge('disk', 'disk percent',["client_no"])
ram_total=Gauge('ram_total', 'ram total',["client_no"])
ram_available=Gauge('ram_available', 'ram available',["client_no"])
ram_used=Gauge('ram_used', 'ram used',["client_no"])
clients_connected=Gauge('clients_connected', 'clients connected')
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
        try:
            data = recv_data(connection)
            if not data:
                clients_connected.dec()
                break
            data = json_parser(data)
            print(data)
            # ram.set(data['ram'])
            ram.labels(client_no=data['client_no']).set(data['ram'])    
            # cpu.set(data['cpu'])
            cpu.labels(client_no=data['client_no']).set(data['cpu'])
            # disk.set(data['disk'])
            disk.labels(client_no=data['client_no']).set(data['disk'])
            # ram_total.set(data['ram_total'])
            ram.labels(client_no=data['client_no']).set(data['ram_total'])
            # ram_available.set(data['ram_available'])
            ram_available.labels(client_no=data['client_no']).set(data['ram_available'])
            # ram_used.set(data['ram_used'])
            ram_used.labels(client_no=data['client_no']).set(data['ram_used'])
            # client_no.set(data['client_no'])
            
            time.sleep(random.randint(1,10))
        except:           
            connection.close()
            clients_connected.dec()
            break    

#main
if __name__== '__main__':
    print("server started at port 45678")
    server=create_server('0.0.0.0',45678)
    start_http_server(1234)
    while True:
        connection,address=accept_client(server)
        clients_connected.inc()
        
        # print_lock.acquire()
        start_new_thread(accpet_client_data, (connection,))
    connection.close()    
        
        

