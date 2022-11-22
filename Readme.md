# Computer Network final project
## Server and Client application with python and socket
Using python and socket to build a server and client application. The server can receive the request from client and send the response to client. The client can send the request to server and receive the response from server.
using Promethus to monitor the server and client application.

## Server
### How to run
1. Open terminal
2. run `python3 server.py`
3. The server will listen on port 45678

## Client
### How to run
1. Open terminal
2. run `python3 client.py`
3. The client will send the request to server and receive the response from server

## Prometheus
1. Prometheus is a monitoring system and time series database. It collects metrics from configured targets at given intervals, evaluates rule expressions, displays the results, and can trigger alerts if some condition is observed to be true.
2. when you run the server and client, you can use prometheus to monitor the server and client application.
3. The prometheus will collect the metrics from the client application and send to server.
4. The server will receive the metrics from client and show the metrics on the prometheus dashboard.
5. The prometheus dashboard will show the metrics of the client application.
6. The prometheus dashboard will be on [here](http://localhost:1234/).
