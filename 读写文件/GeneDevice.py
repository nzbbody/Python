#coding=gb18030

class GeneRules:
    def Gene(self):        
        pFile = open('optdvr.xml','w')

        ss= "<root>\n\t<opt>0</opt>"
        for i in range(10000,10250,1):
            s1="\n\t<device domid=\"52900\" devcode=\"dvr_%d\" parentdomid=\"\" parentdevcode=\"\" orgdomid=\"52900\" orgcode=\"1\" devpath=\"\" orgpath=\"\" devtype=\"1\" manufid=\"1\" title=\"dvr_%d\" status=\"\" devposidx=\"\" updatetime=\"\" loginname=\"admin\" loginpwd=\"admin\" ipaddr=\"10.36.65.80\" portdev=\"%d\" streamtype=\"\" contrator=\"\" locationid=\"\" installspot=\"\" installtime=\"\" maintainer=\"\" phone=\"\" model=\"\" visible=\"\" longitude=\"\" latitude=\"\" desc=\"\" >\n\t\t<channel domid=\"52900\" devcode=\"dvr_%d-chn1\" parentdomid=\"52900\" parentdevcode=\"dvr_%d\" orgdomid=\"\" orgcode=\"\" devpath=\"\" orgpath=\"\" devtype=\"21\" manufid=\"1\" title=\"dvr_%d-chn1\" status=\"\" devposidx=\"\" updatetime=\"\" chnidx=\"\" accesory=\"\" />\n\t</device>\n" %(i,i,i,i,i,i)           
            ss=ss+s1
        ss=ss+"</root>"
        pFile.write(ss)
        pFile.close()

if __name__ == '__main__':
    geneA = GeneRules();
    geneA.Gene();
