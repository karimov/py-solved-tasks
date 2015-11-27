

'''
Ordered sequence
[1,2,3,4,5,,6,7,8,90,]

'''

def binary_search(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if alist[midpoint] < item:
                first = midpoint+1
            else:
                last = midpoint-1

    return found

# Recursive binary search

def rec_binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        first = 0
        last = len(alist)-1
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            return True
        else:
            if alist[midpoint] < item:
                return binary_search(alist[midpoint+1:], item)
            if alist[midpoint] > item:
                return binary_search(alist[:midpoint], item)
