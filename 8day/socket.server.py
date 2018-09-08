import os
import socket

server = socket.socket()
server.bind(('localhost', 8888))

server.listen()

while True:
    conn, addr = server.accept()
    print("new conn:", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行指令:", data)
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output... "

        conn.send(str(len(cmd_res.encode())).encode("utf-8"))
        print("发送数据大小：", len(cmd_res.encode()))
        conn.send(cmd_res.encode("utf-8"))
server.close()
