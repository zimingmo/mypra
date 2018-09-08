import socket

client = socket.socket()
client.connect(('localhost', 6969))
while True:
    msg = input(">>:").strip()

    client.send(msg.encode("utf-8") )

    data = client.recv(1024)
    print("recv:", data.decode())

client.close()