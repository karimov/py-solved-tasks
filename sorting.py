


'''
Bubble sorting
ex: [2,6,4,9,1,7,6,3]

1-pass through:
    [2,4,6,9,1,7,6,3]
2-pass:
    [2,4,6,1,9,7,6,3]
n-1 pass:
    ...
'''

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for j in range(passnum):
            if alist[j] > alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp

'''
shirt bubble
'''

def shortBubble(alist):
    exchange = True
    passnum = len(alist)-1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchange = True
                alist[i],alist[i+1] = alist[i+1], alist[i]
        passnum -= 1

'''
selection sorting
'''
def selectSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionMax = 0
        for position in range(1,fillslot+1):
            if alist[position] > alist[positionMax]:
                positionMax = position

        temp = alist[fillslot]
        alist[fillslot] = alist[positionMax]
        alist[positionMax] = templist

'''
Insertion sort
'''

def insertSort(alist):
    for index in range(1,len(alist)):
        currentValue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentValue:
            alist[position] = alist[position-1]
            position -= 1

        alist[position] = currentValue


'''
Shell sort
'''

def shellSort(alist):
    subListcount = len(alist)//3
    while subListcount > 0:
        for startposition in range(subListcount):
            getInsertionSort(alist, startposition, subListcount)
            print("After increments of size",subListcount,
                                            "This list is",alist)

        subListcount = subListcount//3

def getInsertionSort(alist, start, gap):
    for i in range(start+gap,len(alist), gap):
        currentValue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentValue:
            alist[position] = alist[position-gap]
            position -= gap

        alist[position] = currentValue
