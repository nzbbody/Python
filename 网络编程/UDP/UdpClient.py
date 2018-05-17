import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("udp client start")
while True:
    senddata = raw_input("input UdpClient Send:")
    print("UdpClient[***] Send UdpServer[(\"10.36.65.80\", 5555)]: %s" %(bytes(senddata)))    
    client.sendto(bytes(senddata),("10.36.65.80", 5555))
    
    
    recvdata,serveraddr = client.recvfrom(1024)
    text = str(recvdata)
    print("UdpClient[***] Recv Server[%s]: %s" %(serveraddr,text))
    
    if senddata == "quit":
        break
    
print("udp client finish")
client.close()
