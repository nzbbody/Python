#encoding = utf-8
import socket
import traceback


print ("UDP Receiver Start")

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
client.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
client.bind(('10.65.200.174',5050))



for i in range(1,100):
    try:        
        #senddata = raw_input("input UdpClient Send:")
        #print("Send[%s] : %s" %(serveraddr,bytes(senddata)))
        #client.sendto(senddata,serveraddr)

        recvdata,serveraddr = client.recvfrom(1024)
        text = str(recvdata)
        print("Recv[%s]: %s" %(serveraddr,text))

        #print(recvdata)
        
    except(KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()
