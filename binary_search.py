

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

    if found:
        return True
    else:
        return False

# Recursive binary search

def rec_binary_search(alist, item):
    return _binary_search(alist, 0, len(alist)-1, item)

def _binary_search(alist, first, last, item):
    mid = (first+last)//2
    if first > last:
        return False
    else:
        if alist[mid] == item:
            return True
        else:
            if alist[mid] > item:
                return _binary_search(alist, first, mid-1, item)
            else:
                return _binary_search(alist, mid+1, last, item)


'''
recursive binary search
with slice operator
'''

def rec_binary_search_v1(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist)//2
        if alist[mid] == item:
            return True
        else:
            if alist[mid] > item:
                return rec_binary_search_v1(alist[:mid], item)
            else:
                return rec_binary_search_v1(alist[mid+1:], item)
