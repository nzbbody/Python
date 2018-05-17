#! /usr/bin/env python
# -*- coding: utf-8 -*-
from sort import HeapSort

def Test(aList):
    for i in range(len(aList)):
        if(i != aList[i]):
            print 'Sort Error'
            break
    if(i == len(aList)-1):
        print 'Sort Ok'


aList=[12,6,1,5,3,13,0,8,4,14,9,7,10,15,11,2]
#aList=[6,1,3,0,4,2,5,7]
#sort.BubbleSort(aList)
#sort.SelectSort(aList)
#sort.InsertSort(aList)
#sort.ShellSort(aList)
HeapSort(aList)
Test(aList)

for i in range(5,1,-1):
    print i





