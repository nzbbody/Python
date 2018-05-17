# -*- coding:utf-8 -*-

def FindKMax_BySelect(aList,k):
    for i in range(0,k):
        maxValue_Index=i
        for j in range(i,len(aList),1):
            if(aList[maxValue_Index]<aList[j]):
                maxValue_Index=j
                
        if(maxValue_Index!=i):
            aList[maxValue_Index],aList[i]=aList[i],aList[maxValue_Index]


def FindKMax_ByBubble(aList,k):
    for i in range(0,k):
        for j in range(i,len(aList)-i-1,1):
            if(aList[j]>aList[j+1]):
                aList[j],aList[j+1] = aList[j+1],aList[j]


#查找最大的K个数，正常的冒泡排序，从小到大，最大的K个数沉到最下面，
#反向排序，只需要修改if(aList[j]<aList[j+1])即可
#但是 要想最大的K个数在前面，需要从后向前，把最大的数沉到前面
def FindKMax_ByBubble_2(aList,k):
    for i in range(0,k):
        for j in range(len(aList)-2,i-1,-1):
            if(aList[j]<aList[j+1]):
                aList[j],aList[j+1] = aList[j+1],aList[j]

'''
#上面算法的时间复杂度是O(n*k)，有没有更好的算法呢？
#思考快速排序，从大到小，每次把列表分成两段，前面一段都大于当前值，后面一段都小于当前值
#对快速排序变形，记录分割后的下标，
#如果下标Index大于K，说明，这一次分割，前面一段是Index个最大的值，要从前面一段再分隔，去掉一些较小的数，
#如果下标Index小于K，说明，这一次分割，前面一段是Index个最大的值，要从后面再抽取一些大的数
'''

#分割成两端，并且返回下标，这里是闭区间
def Partition(aList,left,right):
    i =left
    j =right
    target=aList[i]

    while(i<j):
        while(i<j and aList[j]<target):
            j=j-1
        if(i<j):
            aList[i]=aList[j]
            i=i+1

        while(i<j and aList[i]>target):
            i=i+1
        if(i<j):
            aList[j]=aList[i]
            j=j-1
    aList[i]=target
    return i

def FindKMax_ByQuickSort(aList,left,right,k):
    #每次分割后下标
    index=0
    #相当于这一次的分割，处于第几个位置，取决于当前分割的left，因为每次分割的目标段都是不一样的。
    n=0
    if(left<right):
        index=Partition(aList,left,right)
        n=index-left+1

        # 分割的刚刚好
        if(n==k):
            return index
        # 前面一段分割的大数太多了，继续分割前一段，去掉小的数
        elif(n>k):
            return FindKMax_ByQuickSort(aList,left,index,k)
        # 前面一段分割的大数太少了，不够k个，在后面一段中，再分割出k-n个最大的数
        else:
            return FindKMax_ByQuickSort(aList,index+1,right,k-n)


# 统计比x大的元素个数
def FindNumBigThanX(aList,x):
    num=0
    for i in range(len(aList)):
        if (aList[i]>x):
            num+=1
    return num

'''
查找出最大的k个数，我只有找到一个数x，在集合中比x大的个数是k就行了，然后遍历集合，筛选出比x大的数。
注意：这里不要求集合中一定存在元素x，举例来说，集合5,3,200,1,4,80,2找出最大的两个数，
我们知道第3大的数是5，但是我们不需要找出5，找出56，也就是x=56，也是满足条件的。
那么问题来了，如何确定x呢？
思路是我假定x为(max+min)/2，遍历集合，统计比x大的个数。
如果个数>k, 说明我假定的x太小了，
如果个数<k, 说明我假定的x太大了，
这是典型的牛顿迭代问题。
'''
def FindKthMax(aList,k):
    min=0
    max=1000
    x=(min+max)/2
    num=FindNumBigThanX(aList,x)

    while(num != k-1):
        if(num>k-1): # x假定的太小了
            min=x
        else:       # x假定的太大了
            max=x
        x=(min+max)/2
        num=FindNumBigThanX(aList,x)
    return x

# 上面的方法求出的x可能不在集合中，只是保证在集合中比x大的个数是k。
# 如何保证求出的x在集合中呢？
# 上面循环结束的条件是 num != k-1，也就是比x大的个数满足条件就退出。
# 这里应该修改为 把x限定为很小的一个范围内，对于整数范围是1，只要大于1，就继续循环
def FindKthMax_2(aList,k):
    min=0
    max=1000

    while(max-min>1):
        x=(min+max)/2
        num=FindNumBigThanX(aList,x)

        if(num>k-1): # x假定的太小了
            min=x
        else:       # x假定的太大了
            max=x
    return x

def FindKMax_ByKth(aList,k):
    # 找出最大的k个数，先找出第k+1大的数
    x=FindKthMax_2(aList,k+1)
    for i in range(len(aList)):
        if aList[i]>x:
            print aList[i]

'''
使用最小堆，思路是建立一个k个元素的最小堆，堆顶是最小值，遍历集合与堆顶比较，
如果比堆顶大，说明应该踢出堆顶元素，新的元素进入，重新调整堆。
举个例子，公司调整干部序列，目前的干部序列最差的排在前面，遍历员工，如果当前员工
比最差的干部强，踢出最差的干部，当前员工进入干部序列，并重新调整干部序列，最差的干部
在最前面。
'''
def HeapAdjust(aList,curIndex,size):
    lChildIndex=2*curIndex+1
    rChildIndex=2*curIndex+2

    if(lChildIndex<size):
        if(rChildIndex<size):
            if(aList[lChildIndex]<aList[rChildIndex]):
                if(aList[lChildIndex]<aList[curIndex]):
                    aList[lChildIndex],aList[curIndex]=aList[curIndex],aList[lChildIndex]
                    HeapAdjust(aList,lChildIndex,size)
            else:
                if(aList[rChildIndex]<aList[curIndex]):
                    aList[rChildIndex],aList[curIndex]=aList[curIndex],aList[rChildIndex]
                    HeapAdjust(aList,rChildIndex,size)
        else:
             if(aList[lChildIndex]<aList[curIndex]):
                    aList[lChildIndex],aList[curIndex]=aList[curIndex],aList[lChildIndex]
                    HeapAdjust(aList,lChildIndex,size)

def FindKMax_ByHeap(aList,k,bList):
    for i in range(k):
        bList.append(aList[i])

    start=len(bList)/2-1
    for i in range(start,-1,-1):
        HeapAdjust(bList,i,len(bList))

    for i in range(k,len(aList),1):
        if(aList[i]>bList[0]):
            bList[0]=aList[i]
            HeapAdjust(bList,0,len(bList))
        
aList=[3,5,2,7,6,4,9,10,1,105,58]
print aList

#FindKMax_BySelect(aList,5)
#FindKMax_ByBubble_2(aList,5)
#FindKMax_ByQuickSort(aList,0,len(aList)-1,4)
#FindKMax_ByKth(aList,2)
bList=[]
FindKMax_ByHeap(aList,4,bList)
print bList
#print x
#print aList






















