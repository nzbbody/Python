#coding=utf8
from datetime import *

curDateTime=datetime.now()
print curDateTime;
curDateTime=curDateTime.replace(hour=10);
curDateTime=curDateTime.replace(minute=20);
curDateTime=curDateTime.replace(second=0);
print curDateTime;

aFile=open('time_template.txt','w');

for i in range(1,10,1):
    ss = "<Time>%d:%d:00-%d:%d:00</Time>" \
         %(curDateTime.hour,curDateTime.minute,curDateTime.hour,curDateTime.minute+5)
    curDateTime=curDateTime+timedelta(minutes=5)
    aFile.write(ss)
aFile.close()

    
    
