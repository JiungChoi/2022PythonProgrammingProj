import sys
def selectionSort(alist):
    for i in range(len(alist)):
        minPos = getMinPos(alist, i)
        temp = alist[minPos]
        alist[minPos] = alist[i]
        alist[i] = temp
    return alist
        
def getMinPos(alist, start):
    minPos = start
    for i in range(start + 1, len(alist)):
        if alist[i] < alist[minPos]:
            minPos = i
    return minPos

def binarySearch(alist, find_num):
    start = 0
    end = len(alist) -1
    
    while (start<=end):
        mid = (start + end )// 2
        if alist[mid] > find_num: end = mid -1
        elif alist[mid] == find_num : return "yes"
        else : start = mid + 1
    return "no"

def isExist(my_item, order_item):
    isExistAry = []
    
    for i in range(len(order_item)):
        isExistAry.append(binarySearch(my_item, order_item[i]))
    
    return isExistAry

N = sys.stdin.readline()
my_item = selectionSort(list(map(int, sys.stdin.readline().split())))
M = sys.stdin.readline()
order_item = selectionSort(list(map(int, sys.stdin.readline().split())))



print(isExist(my_item, order_item))