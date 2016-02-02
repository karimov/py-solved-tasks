from node import UnorderedList

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.loadf = 0
        self.treshold = 0.75

    def updateLoadf(self):
        used = [i for i in self.slots if i != None]
        self.loadf = float(len(used))/float(self.size)

#Chaining Collision Resolution

    def put_v2(self, key, data):
        hashValue = self.hashFunction(key, len(self.slots))

        if self.slots[hashValue] == None:
            refKey = UnorderedList()
            refData = UnorderedList()
            self.slots[hashValue] = refKey
            refKey.append_v2(key)
            self.data[hashValue] = refData
            refData.append_v2(data)
        else:
            refKey = self.slots[hashValue]
            refData = self.data[hashValue]
            if refKey.index(key) != None:
                refData[refKey.index(key)] = data
            else:
                refKey.append_v2(key)
                refData.append_v2(data)

    def get_v2(self, key):
        hashValue = self.hashFunction(key, len(self.slots))

        if self.slots[hashValue] != None:
            refKey = self.slots[hashValue]
            refData = self.data[hashValue]
            return refData[refKey.index(key)]
        else:
            return None

    def delete_v2(self, key):
        hashValue = self.hashFunction(key, len(self.slots))

        if self.slots[hashValue] != None:
            refKey = self.slots[hashValue]
            refData = self.data[hashValue]

            tmp = refKey.index(key)
            refKey.remove(key)
            refData.remove(refData[tmp])
        else:
            return None

    def resize(self, new_size):
        for slot in range(new_size):
            self.slots.append(None)
            self.data.append(None)

        self.size += new_size
        self.updateLoadf()

        for i in range(self.size):
            if self.slots[i] != None and self.data[i] != None:
               key = self.slots[i]
               value = self.data[i]
               self.put(key, value)

    def put(self, key, data):
        if self.loadf >= self.treshold:
            self.resize(self.size*2)

        hashValue = self.hashFunction(key, len(self.slots))

        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
            self.updateLoadf()
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
                    self.updateLoadf()
                else:
                    self.data[nextslot] = data  # update

    def hashFunction(self, key, size):
        return key%size

    def rehash(self, oldhashValue, size):
        if oldhashValue >= 1:
            oldhashValue += 2
        if oldhashValue == 0:
            oldhashValue += 1
        return (oldhashValue)%size

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
        return self.get_v2(key)

    def __setitem__(self, key, data):
        self.put_v2(key, data)

    def delete(self, key):
        hashValue = self.hashFunction(key, len(self.slots))

        position = hashValue
        stop = False
        found = False
        while self.slots[position] != None and not stop:
            if self.slots[position] == key:
                self.slots[position] = None
                self.data[position] = None
                self.updateLoadf()
            else:
                position = self.rehash(hashValue, len(self.slots))
                if position == hashValue:
                    stop = True

    def __delitem__(self, key):
        self.delete_v2(key)

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
