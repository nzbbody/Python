def BubbleSort(aList):
    for i in range(len(aList)):
        for j in range(len(aList)-1-i):
            if aList[j]>aList[j+1]:
                tmp = aList[j]
                aList[j] = aList[j+1]
                aList[j+1]=tmp
    print(aList)
    
