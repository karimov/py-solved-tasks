

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def setNext(self, obj):
        self.next = obj


class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        items = '['
        while current != None:
            items += str(current.getData())+","
            current = current.getNext()
        items += "]"
        return str(items)

    def __repr__(self):
        head = self.head
        item = []
        while head != None:
            item.append(head.getData())
            head = head.getNext()

        return repr(item)

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = self.head
        self.head = Node(item)
        self.head.setNext(temp)
        self.length += 1

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def size_v2(self):
        return self.length

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if not found:
            print "Item not found"
        elif previous == None:
            self.head = current.getNext()
            self.length -= 1
        else:
            previous.setNext(current.getNext())
            self.length -= 1

    def append(self, item):
        current = self.head
        previous = None
        last = Node(item)
        while current != None:
            previous = current
            current = current.getNext()

        if previous == None:
            self.head = last
            self.length += 1
        else:
            previous.setNext(last)
            self.length += 1

    def insert(self, pos, item):
        current = self.head
        previous = None
        indexer = 0
        inItem = Node(item)
        while current != None and indexer < pos:
            previous = current
            current = current.getNext()
            indexer += 1

        if previous == None:
            inItem.setNext(current)
            self.head = inItem
            self.length += 1
        else:
            previous.setNext(inItem)
            inItem.setNext(current)
            self.length += 1

    def index(self, item):
        current = self.head
        indexer = 0
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                indexer += 1

        if current == None:
            print("%d is not in list" %(item))
        else:
            return indexer


    def pop(self, pos):
        current = self.head
        previous = None
        indexer = 0
        while current != None and indexer < pos:
            previous = current
            current = current.getNext()
            indexer += 1

        if previous == None:
            self.head = current.getNext()
            self.length -= 1
        else:
            previous.setNext(current.getNext())
            self.length -= 1

        return current.getData()

    def append_v2(self, item):
        head = self.head
        tail = self.tail
        rear = Node(item)
        if head == None:
            self.head = rear
            self.tail = rear
            self.length += 1
        if tail:
            tail.setNext(rear)
            self.tail = rear
            self.length += 1

    def add_v2(self, item):
        node = Node(item)
        head = self.head
        tail = self.tail

        if head == None:
            self.head = self.tail = node
            self.length += 1
        if head:
            node.setNext(head)
            self.head = node
            self.length += 1

    def pop(self):
        current = self.head
        previous = None
        pos = 1
        while pos < self.size():
            previous = current
            current = current.getNext()
            pos += 1

        if previous == None:
            self.head = None
            self.length -= 1
        else:
            previous.setNext(None)
            self.length -= 1

        return current.getData()

    def pop_v2(self):
        pass


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        counter = 0
        while current != None:
            current = current.getNext()
            counter += 1

        return counter

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if curremt.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if not found:
            print("Item not found")
        elif previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() < item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        node = Node(item)
        if previous == None:
            node.setNext(current)
            self.head = node
        else:
            node.setNext(current)
            previous.setNext(node)


class ImprovedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        counter = 0
        while current != None:
            current = current.getNext()
            counter += 1

        return counter

    def enqueue(self, item):
        head = self.head
        tail = self.tail
        node = Node(item)
        if head == None:
            self.head = self.tail = node
        if tail:
            tail.setNext(node)
            self.tail = node

    def dequeue(self):
        head = self.head
        if head:
            self.head = head.getNext()
        return head.getData()


class StackLinkedList:
    def __init__(self):
        self.bottom = None
        self.length = 0

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        bottom = self.bottom
        basement = None
        topFound = False
        node = Node(item)
        while bottom != None and not topFound:
            if not bottom.getNext():
                topFound = True
            else:
                basement = bottom
                bottom = bottom.getNext()

        if bottom == None:
            self.bottom = node
            self.length += 1
        else:
            bottom.setNext(node)
            self.length += 1

    def pop(self):
        bottom = self.bottom
        basement = None
        topFound = False
        while bottom != None and not topFound:
            if not bottom.getNext():
                topFound = True
            else:
                basement = bottom
                bottom = bottom.getNext()

        if basement == None:
            self.bottom = None
            self.length -= 1
        else:
            basement.setNext(None)
            self.length -= 1

        return bottom.getData()

    def peek(self):
        bottom = self.bottom
        topFound = False
        while bottom != None and not topFound:
            if bottom.getNext() == None:
                topFound = True
            else:
                bottom = bottom.getNext()
        return bottom.getData()

    def size(self):
        if self.length < 0:
            return 0
        return self.length
