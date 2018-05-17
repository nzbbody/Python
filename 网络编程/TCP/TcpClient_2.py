#coding=utf8
import socket
import threading
from time import ctime,sleep

HOST='10.36.65.80'
PORT=50007


def HandleRecv(s):
       while 1:
              data=s.recv(1024)  #把接收的数据定义为变量
              print data         #输出变量
              #sleep(1)

def HandleSend(s):
       while 1:
              cmd=raw_input("Please input cmd:")       #与人交互，输入命令
              #cmd='fuck'
              s.sendall(cmd)      #把命令发送给对端
              sleep(1)



s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
#s.bind((HOST,50008))          #套接字绑定的IP与端口，
s.connect((HOST,PORT))       #要连接的IP与端口
recv = threading.Thread(target=HandleRecv,args=(s,))
recv.start()

send = threading.Thread(target=HandleSend,args=(s,))
send.start()

'''
while 1:
       cmd=raw_input("Please input cmd:")       #与人交互，输入命令
       s.sendall(cmd)      #把命令发送给对端
       
       #data=s.recv(1024)     #把接收的数据定义为变量
       #print data         #输出变量
s.close()   #关闭连接
'''
