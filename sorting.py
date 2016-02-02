


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
        alist[positionMax] = temp

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

'''
Merge sort
'''

def mergeSort(alist):
#    print("Spliting ", alist)
    if len(alist) > 1:
        mid = len(alist)//2

        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i,j,k = 0,0,0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
#        print("Merging ", alist)


'''
Merge sorting without slice operator
'''

def mergeSort_noslice(alist):
    _merge(alist, 0, len(alist)-1)

def _merge(alist, first, last):
    print("Splitting ",alist[first:last+1])
    mid = (first+last)//2
    if first < last:
        _merge(alist, first, mid)
        _merge(alist, mid+1, last)

        i = first
        j = mid+1
        k = 0
        while i <= mid and j <= last:
            if alist[i] < alist[j]:
                alist[k] = alist[i]
                i = i + 1
            else:
                alist[k] = alist[j]
                j = j +1
            k = k + 1

        while i <= mid:
            alist[k] = alist[i]
            i = i + 1
            k = k + 1

        while j <= last:
            alist[k] = alist[j]
            j = j + 1
            k = k +1
        print("Merging ", alist)

'''
Quick sort
'''

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if first < last:

        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)

def partition(alist, first, last):
    f,m,l = alist[first],alist[(first+last)//2],alist[last]
    pivotvalue = median_of_three([f,m,l])

    leftmark = first
    rightmark = last

    done = False
    while not done:

        while alist[leftmark] < pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] > pivotvalue:
            rightmark = rightmark - 1

        if alist[leftmark] == pivotvalue or alist[rightmark] == pivotvalue:
            done = True
        else:
            tmp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = tmp

    if alist[leftmark] == pivotvalue:
        tmp = alist[leftmark]
        alist[leftmark] = alist[rightmark]
        alist[rightmark] = tmp
    else:
        tmp = alist[rightmark]
        alist[rightmark] = alist[leftmark]
        alist[leftmark] = tmp

    return pivotvalue

def median_of_three(mlist):
    result = mlist
    bubbleSort(result)
    return result[1]

'''
Quick sort variation
'''

def partition_q(alist):
    pivot = alist[0]
    less,equal,greater = [],[],[]
    for i in alist:
        if i < pivot:
            less.append(i)
        if i > pivot:
            greater.append(i)
        if i == pivot:
            equal.append(i)

    return less, equal, greater

def quickSort2(alist):
    if alist:
        less, equal, greater = partition_q(alist)
        return quickSort2(less) + equal + quickSort2(greater)
    return alist
