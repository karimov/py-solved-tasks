'''
Binary Heep Implementation
'''

class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        self._maxSize = 10

    def setmaxSize(self, size):
        self._maxSize = size

# percolate method

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2

    def percMaxup(self, i):
        while i//2 > 0:
            if self.heapList[i] > self.heapList[i//2]:
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i = i//2

#insert new item 

    def insert(self, k):
        if self.currentSize < self._maxSize:
            self._insert(k)
        else:
            self.delMin()
            self._insert(k)

    def _insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

# before to delete minimum item 
# of binary heap

    def percDown(self, i):
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc

    def percMaxdown(self, i):
        while (i*2) <= self.currentSize:
            mx = self.maxChild(i)
            if self.heapList[i] < self.heapList[mx]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mx]
                self.heapList[mx] = temp
            i = mx

    def minChild(self, i):
        if i*2+1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def maxChild(self, i):
        if 2*i+1 > self.currentSize:
            return 2*i
        else:
            if self.heapList[2*i] < self.heapList[2*i+1]:
                return 2*i+1
            else:
                return 2*i

# delete method itself

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def delMax(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percMaxdown(1)
        return retval

# build heap method

    def buildMinHeap(self, alist):
        i = len(alist)//2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i = i - 1

    def buildMaxHeap(self, alist):
        i = len(alist)//2
        self.heapList = [0] + alist[:]
        self.currentSize = len(alist)
        while i > 0:
            self.percMaxdown(i)
            i = i - 1

    def heapSort(self, alist):
        self.buildMinHeap(alist)
        sortedList = []
        pos = self.currentSize
        while pos != len(sortedList):
            sortedList.append(self.delMin())

        return sortedList


'''
 Using the BinaryHeap class, implement a new class called PriorityQueue. Your PriorityQueue class should implement the constructor, plus the enqueue and dequeue methods.
 '''
class PriorityQueue(BinaryHeap):
    def __init__(self):
        BinaryHeap.__init__(self)

    def enqueue(self, value):
        self.insert(value)

    def dequeue(self):
        return self.delMin()
