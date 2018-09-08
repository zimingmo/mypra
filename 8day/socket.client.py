import socket


client = socket.socket()

client.connect(('localhost', 8888))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024)
   #  print("接受数据大小:", cmd_res_size)
   #  received_size = 0
   #  received_data =b''
   #  while received_size < int(cmd_res_size.decode()):
   #      data = client.recv(1024)
   #      received_size += len(data)
   #      received_data += data
   # # cmd_res = client.recv(1024)
   #
   #  # print(cmd_res.decode())
   #  # print(len(cmd_res))
   #  else:
   #      print("cmd res receive done...", received_size)
    print(cmd_res_size.decode())
client.close()
