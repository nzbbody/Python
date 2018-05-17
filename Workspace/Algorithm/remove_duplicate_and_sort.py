def HandleByDict(aStr):
    print(aStr)
    aDict={}
    for i in aStr:
        if(aDict.has_key(i)):
            aDict[i]+=1
        else:
            aDict[i]=1

    aDict=sorted(aDict.iteritems(),key=lambda d:d[0])

    for i in aDict:
        print i

def HandleByHashTable(aStr):
    print aStr
    aList=[]
    for i in range(512):
        aList.append(0)
        
    for i in aStr:
        aList[ord(i)]+=1

    for i in range(len(aList)):
        if(aList[i] != 0):
            print chr(i),":", aList[i]


aStr="acbbdkdehfghgefahb"
HandleByDict(aStr)
HandleByHashTable(aStr)









