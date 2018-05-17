#coding=gb18030

class GeneRules:
    def Gene(self):        
        pFile = open('rules.xml','w')

        for i in range(1,66,1):
            ss= "<radiometryrule><id>%d</id><enable>1</enable><presetid>%d</presetid><ruleid>%d</ruleid><name>dian_%d</name><metertype>1</metertype><coordinatecount>1</coordinatecount><point x=\"1000\" y=\"%d\"/><sampleperiod>0</sampleperiod><alarmsetcount>1</alarmsetcount><radiometryalarmset id=\"0\" enable=\"0\" resulttype=\"0\" alarmcondition=\"0\" threshold=\"20.0\" hysteresis=\"0.1\" duration=\"30\"/><radiometrylocalparam enable=\"0\" objectemissivity=\"0.000000\" objectdistance=\"0\" refalectedtemp=\"0\"/></radiometryrule>\n" %(i,i/8+1,i%8,i,i*100)
            pFile.write(ss)
        pFile.close()

if __name__ == '__main__':
    geneA = GeneRules();
    geneA.Gene();
