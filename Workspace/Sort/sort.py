#! /usr/bin/env python
# -*- coding: utf-8 -*-

def BubbleSort(aList):
    listLen=len(aList)
    for i in range(0,listLen,1):
        for j in range(0,listLen-i-1,1):
            if aList[j]>aList[j+1]:
                aList[j],aList[j+1]=aList[j+1],aList[j]

def SelectSort(aList):
    for i in range(len(aList)):
        minIndex=i
        for j in range(i+1,len(aList)):
            if(aList[minIndex]>aList[j]):
                minIndex=j
        aList[minIndex],aList[i]=aList[i],aList[minIndex]

def InsertSort(aList):
    for i in range(1,len(aList),1):
        curValue=aList[i]
        while(i>0 and aList[i-1]>curValue):
            aList[i]=aList[i-1]
            i=i-1
        aList[i]=curValue

def ShellSort(aList):
    interval=len(aList)
    while(True):
        interval=interval/3+1
        for i in range(interval,len(aList),1):
            curValue=aList[i]
            while(i>interval-1 and aList[i-interval]>curValue):
                aList[i]=aList[i-interval]
                i=i-interval
            aList[i]=curValue
        if(interval==1):
            break

# 递归
def HeapAdjust(aList,curIndex,size):
    lChildIndex=2*curIndex+1
    rChildIndex=2*curIndex+2

    if(lChildIndex<size):
        if(rChildIndex<size):
            if(aList[lChildIndex]>aList[rChildIndex]):
                if(aList[lChildIndex]>aList[curIndex]):
                    aList[lChildIndex],aList[curIndex]=aList[curIndex],aList[lChildIndex]
                    HeapAdjust(aList,lChildIndex,size)
            else:
                if(aList[rChildIndex]>aList[curIndex]):
                    aList[rChildIndex],aList[curIndex]=aList[curIndex],aList[rChildIndex]
                    HeapAdjust(aList,rChildIndex,size)
        else:
             if(aList[lChildIndex]>aList[curIndex]):
                    aList[lChildIndex],aList[curIndex]=aList[curIndex],aList[lChildIndex]
                    HeapAdjust(aList,lChildIndex,size)

# While
def HeapAdjust_2(aList,curIndex,size):

    while(curIndex<size):
        lChildIndex=2*curIndex+1
        rChildIndex=2*curIndex+2

        if(lChildIndex<size):
            if(rChildIndex<size):
                if(aList[lChildIndex]>aList[rChildIndex]):
                    if(aList[lChildIndex]>aList[curIndex]):
                        aList[lChildIndex],aList[curIndex]=aList[curIndex],aList[lChildIndex]
                        curIndex=lChildIndex
                    else:
                        break
                else:
                    if(aList[rChildIndex]>aList[curIndex]):
                        aList[rChildIndex],aList[curIndex]=aList[curIndex],aList[rChildIndex]
                        curIndex=rChildIndex
                    else:
                        break
            else:
                 if(aList[lChildIndex]>aList[curIndex]):
                    aList[lChildIndex],aList[curIndex]=aList[curIndex],aList[lChildIndex]
                    curIndex=lChildIndex
                 else:
                    break
        else:
            break

def HeapSort(aList):
    start=len(aList)/2-1
    for i in range(start,-1,-1):
        HeapAdjust_2(aList,i,len(aList))

    for i in range(len(aList)-1):
        aList[0],aList[len(aList)-i-1] = aList[len(aList)-i-1],aList[0]
        HeapAdjust_2(aList,0,len(aList)-i-1)




