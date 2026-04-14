import socket
import json

ip='10.17.31.27'
port=5026
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip,port))

request = {
    "func": "add",
    "a": 5,
    "b": 3
}

client.send(json.dumps(request).encode())

data = client.recv(1024)
response = json.loads(data.decode())

print("Sonuç:", response["result"])
client.close()
