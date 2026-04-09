import socket
socket_server=socket.socket()#创建对象
socket_server.bind(("localhost",8888))#对象信息，二元元组（ip地址，端口）
socket_server.listen(1)#监听数//链接数
con,address=socket_server.accept()#accept：阻断函数，返回二元元组//不运行代码卡在这里，con，address解构赋值,
print(f"地址信息：{address}")
while True:
    data=con.recv(1024).decode("UTF-8")#recv：缓冲区，decode：字节数组（bytes）解码为字符串
    print(f"发送消息：{data}")
    msg=input("回复信息：")#encode：与decode相反，字符串转化为字节数组
    if msg=="exit":
        break
    con.send(msg.encode("UTF-8"))
socket_server.close()

