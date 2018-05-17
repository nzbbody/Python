#coding=gb18030
from xml.etree.ElementTree import *;
class XmlGene:
    def GeneXml(self):        
        Simulators = Element('Simulators');
        #ipList = ['10.36.65.55','10.36.65.25','10.36.65.24','10.36.65.89','10.36.65.15','10.36.65.91','10.36.65.60','10.36.65.112'];

        ipList = ['10.36.65.89'];
        
        simulatorId = 0;
        for ip in ipList:
            port = 37777;        
            for i in range(0,40):            
                simulator = Element('Simulator', {'id': str(simulatorId)});
                SubElement(simulator, 'Name',{'value': ip});
                SubElement(simulator, 'DeviceIP',{'value': ip});
                SubElement(simulator, 'DevicePort',{'value': str(port)});
                SubElement(simulator, 'UserName',{'value': ''});
                SubElement(simulator, 'Password',{'value': ''});
            
                ChannelList = Element('ChannelList');
                channelId = 0;
                for i in range(0,16):                
                    Channel = Element('Channel', {'id': str(channelId),'name': 'XXXtongdaoXXX'+str(channelId)});
                    ChannelList.append(Channel);
                    channelId = channelId+1;

                simulator.append(ChannelList);
                Simulators.append(simulator);
                port = port+1;
                simulatorId = simulatorId+1;
        
        simulateXml = ElementTree();
        simulateXml._setroot(Simulators);
        simulateXml.write('Simulate.xml','utf-8');   

if __name__ == '__main__':
    geneA = XmlGene();
    geneA.GeneXml();
