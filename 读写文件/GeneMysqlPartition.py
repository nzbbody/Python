#coding=gb18030
from datetime import *
class GeneMysqlPartition:
    def Gene(self):        
        pFile = open('MysqlPartition.txt','w')
        i=0
        curDate=date.today()
        while(i<500):
            ss= "partition p%d values less than (to_days('%s-%s-%s')),\n" %(i,curDate.year,curDate.month,curDate.day)
            pFile.write(ss)
            i=i+1
            curDate=curDate+timedelta(days=7)
        pFile.close()

if __name__ == '__main__':
    geneA = GeneMysqlPartition();
    geneA.Gene();
