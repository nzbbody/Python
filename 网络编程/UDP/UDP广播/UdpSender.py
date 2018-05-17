import socket, traceback

print ("UDP Sender Start")

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

target = ('255.255.255.255',5050);

# ¹ã²¥·¢ËÍ
senddata = raw_input("input Multi Data:")
print("Multi Send To Target[%s]: %s" %(target,bytes(senddata)))
server.sendto(senddata,target)

for i in range(1,100):
    try:
        senddata = raw_input("input Multi Data:")
        print("Multi Send To Target[%s]: %s" %(target,bytes(senddata)))
        server.sendto(senddata,target)

        #recvdata,clientaddr = server.recvfrom(1024)
        #text = str(recvdata)
        #print("Recv From Target[%s]: %s" %(clientaddr,text))
    except(KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()
