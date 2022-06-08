import socket
import json
import psutil

# connect to server
def connect(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
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
    client=connect('0.0.0.0',8080)
    data=read_data()
    JSON=json_convert(data)
    send(client,JSON)
    
    


    
    