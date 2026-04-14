import socket
import json

def  add(a,b):
	return a+b
ip='10.17.31.232'
port=5026
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(1)

conn, addr = server.accept()

data = conn.recv(1024)
request = json.loads(data.decode())

if request["func"] == "add":
    result = add(request["a"], request["b"])

response = json.dumps({"result": result})
conn.send(response.encode())

conn.close()
