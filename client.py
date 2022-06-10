import socket
import json
from tkinter.tix import Tree
import psutil
import time
# connect to server
def connect(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    print("Connected to server: "+ip+" : "+str(port))
    return s
#send data to server
def send(s, data):
    s.send(data.encode())
#read system data
def read_data():
    data = {}
    data['cpu'] = psutil.cpu_percent(interval=1)
    data['ram'] = psutil.virtual_memory().percent
    data['disk'] = psutil.disk_usage('/').percent
    data['ram_total'] = psutil.virtual_memory().total
    data["ram_available"] = psutil.virtual_memory().available
    data['ram_used']=psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
    return data
#convert data to json
def json_convert (data):
    return json.dumps(data)
#main
if __name__ == '__main__':
    counter =1
    while True:
        try:
            client=connect('127.0.0.1',45678)
            while True :
                data=read_data()
                JSON=json_convert(data)
                send(client,JSON)
                time.sleep(10)
        except:
            print("")
            print(f"can not connect to server attempt {counter}")
            counter+=1
            time.sleep(10)
    


    
    