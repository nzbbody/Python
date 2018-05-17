import os
target_path="D:/test"
print target_path
fileList = os.listdir(target_path)
print fileList

for a in fileList:
    postfix=a.split(".")[1]
    
    if postfix == "h" or postfix == "cpp":        
        os.rename(target_path+"/"+a,target_path+"/"+a.replace("vms","dmu"))   
    

            
        
    
        
