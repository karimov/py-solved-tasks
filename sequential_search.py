

#Unordered sequence 

def seq_search(alist, item):
    found = False
    pos = 0
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    if not found:
        return False
    else:
        return True

#Ordered sequence

def seq_search_ord(alist, item):
    found = False
    stop = False
    pos = 0
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    if found:
        return found
    else:
        return not found
