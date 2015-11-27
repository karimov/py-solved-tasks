

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashValue = self.hashFunction(key, len(self.slots))

        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = data  # update
            else:
                nextslot = self.rehash(hashValue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # update

    def hashFunction(self, key, size):
        return key%size

    def rehash(self, oldhashValue, size):
        return (oldhashValue+1)%size

    def get(self, key):
        startslot = self.hashFunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def delete(self, key):
        hashValue = self.hashFunction(key, len(self.slots))

        position = hashValue
        stop = False
        found = False
        while self.slots[position] != None and not stop:
            if self.slots[position] == key:
                self.slots[position] = None
                self.data[position] = None
            else:
                position = self.rehash(hashValue, len(self.slots))
                if position == hashValue:
                    stop = True

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False

    def len(self):
        size = 0
        for i in range(len(self.slots)):
            if self.slots[i] != None:
                size += 1

        return size

    def __len__(self):
        return self.len()
