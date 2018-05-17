import time
class Util:
    def GetData(self,s):
        s2 = s.split(' ')
        bb = []
        for i in s2:
            bb.append(int(i,16))
        return bb

    def PrintRecvData(self,data):
        print('Recv Data From Adapter: ',time.strftime('%m-%d-%H-%M-%S',time.localtime(time.time())))
        self.PrintData(data)

    def PrintSendData(self,data):
        print('Send Data To Adapter: ')
        self.PrintData(data)

    def PrintData(self,data):
        for i in data:
            print('%02X ' %i)
        print()

    def GetCurrTime(self):
        year = int(time.strftime('%Y',time.localtime(time.time())))
        ss =''
        ss = ss+hex(int(year/256))+' '+hex(year%256)
        timeStr = time.strftime('%m-%d-%H-%M-%S',time.localtime(time.time()))
        s1 = timeStr.split('-')
        for i in s1:
            ss= ss+' '+hex(int(i))
        return ss
if __name__ == '__main__':
    util = Util()
    print(util.GetCurrTime())
            
        
    
        
