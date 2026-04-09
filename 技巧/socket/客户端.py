import socket
socket_client=socket.socket()#客户端对象
socket_client.connect(("localhost",8888))#链接服务器
while True:
    msg=input("发送消息：")
    if msg=="exit":
        break
    socket_client.send(msg.encode("UTF-8"))#不同于服务器，客户端不需要accept接受，且对象不变
    recv_data=socket_client.recv(1024)
    print(f"回复信息：{recv_data.decode('UTF-8')}")
socket_client.close()