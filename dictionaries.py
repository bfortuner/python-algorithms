## Implement Python Dictionary ##
## Using Hash Table ##



## Dictionary ##
class Dictionary(object):
    def __init__(self, n):
        self.buckets = n
        self.keys = [None] * n
        self.values = [None] * n

    def __str__(self):
        dict_str = "{"
        for i in range(self.buckets):
            if self.keys[i] != None:
                dict_str += str(self.keys[i]) + ": " + str(self.values[i]) + ", "
        dict_str += "}"
        return dict_str.replace(", }","}")

    def convert_str_to_int(self, str):
        sum = 0
        for e in str:
            sum += ord(e)
        return sum

    def hash_function(self, key):
        if type(key) == str:
            i = self.convert_str_to_int(key) % self.buckets
        else:
            i = key % self.buckets
        return i

    def put(self, key, value):
        i = self.hash_function(key)
        # Insert new key if key != exist
        if self.keys[i] == None:
            self.keys[i] = key
            self.values[i] = value

        # If identical key exists, overwrite value
        elif self.keys[i] == key:
            self.values[i] = value

        # In event of collision, use linear probing
        else:
            placed = False
            while not placed:
                i += 1
                if i >= self.buckets:
                    i = 0
                if self.keys[i] == None:
                    self.keys[i] = key
                    self.values[i] = value
                    placed = True
            return

    def __len__(self):
        count = 0
        for e in self.keys:
            if e == None:
                count += 1
        return self.buckets - count


    def __contains__(self, key):
        for e in self.keys:
            if e == key:
                return True
        return False

    def delete(self, key):
        i = self.hash_function(key)
        if self.keys[i] == key:
            self.keys[i] = None
            self.values[i] = None
        else:
            startpos = i
            i += 1
            found = False
            while not found and i != startpos:
                if i >= self.buckets:
                    i = 0
                if self.keys[i] == key:
                    self.keys[i] = None
                    self.values[i] = None
                    found = True
                i += 1

    def get(self, key):
        i = self.hash_function(key)
        if self.keys[i] == key:
            return self.values[i]
        else:
            found = False
            startpos = i
            i += 1
            while not found and startpos != i:
                if i >= self.buckets:
                    i = 0
                if self.keys[i] == key:
                    return self.values[i]
                i += 1


    def __getitem__(self, key):
        return self.get(key)


    def __setitem__(self, key, value):
        self.put(key, value)

d1 = Dictionary(11)
#print d1
#print d1.buckets
#print d1.keys
#print d1.values
d1.put('hey',2222)
d1.put('brendan',333)
d1.put(12,'colin')
d1.put('eyh',1111)
#print d1.keys
#print d1.values
#print len(d1)
#print 'hey' in d1
print d1.get('hey')
print d1.get('eyh')
d1.delete('hey')
d1.delete('eyh')
print d1
#print d1.get(12)


