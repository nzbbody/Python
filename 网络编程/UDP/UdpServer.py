import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("10.36.65.80",5555))
print("udp server start")
while True:
    recvdata,clientaddr = server.recvfrom(1024)
    text = str(recvdata)
    print("UdpServer[***] Recv Client[%s]: %s" %(clientaddr,text))
    
    
    senddata = raw_input("input UdpServer Send:")
    print("UdpServer[***] Send Client[%s]: %s" %(clientaddr,bytes(senddata)))
    server.sendto(senddata,clientaddr)
    
    #if text == "quit":
    #   break
    
print("udp server finish")
server.close()
