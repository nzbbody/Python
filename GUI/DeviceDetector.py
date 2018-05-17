''''' 
Created on 2014-10-18 
 
@author: Niuzb
'''  
import wx
import wx.grid
class Example(wx.Frame):  
    def __init__(self,parent,title):  
        super(Example,self).__init__(parent,title=title,size=(960,480))  
        self.InitUI()  
        self.Centre()  
        self.Show()  
    def InitUI(self):  
        panel = wx.Panel(self)  
          
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)  
        font.SetPointSize(9)  
          
        vbox = wx.BoxSizer(wx.VERTICAL)

        grid = wx.grid.Grid(panel)
        grid.CreateGrid(10,4)
        grid.SetColLabelValue( 0, "IP" )
        grid.SetColLabelValue( 1, "Port" )
        grid.SetColLabelValue( 2, "LoginName" )
        grid.SetColLabelValue( 3, "Password" )
        grid.SetDefaultColSize(160, resizeExistingCols=True) 
        for row in range(10):
            for col in range(4):
                grid.SetCellValue(row, col,"cell (%d,%d)" % (row, col))       
        vbox.Add(grid, proportion=1, flag=wx.ALIGN_CENTER|wx.ALL,border=10)        

        btn = wx.Button(panel, label='Detect')
        vbox.Add(btn,proportion=0,flag=wx.ALIGN_CENTER|wx.ALL, border=10)

        panel.SetSizer(vbox)  
          
if __name__ == '__main__':  
    app = wx.App()  
    Example(None,title="DeviceDetector[1.0]")  
    app.MainLoop()  
