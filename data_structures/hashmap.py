

class HashMap:
    def __init__(self):
        self.max = 100
        self.table = [None for i in range(self.max)]

    def _hash(self, key):
        h = 0
        for i in str(key):
            h += ord(i)
        return h % self.max

    def add(self, key, value):
        h = self._hash(key)
        i = 0
        # simple linear probing
        while self.table[h+i] and not self.table[h+1][0] == key:
            i += 1
        self.table[h+i] = (key, value)

    def get(self, key):
        h = self._hash(key)
        i = 0
        while self.table[h+i][0] != key:
            i += 1
        return self.table[h+i][1]




if __name__ == "__main__":
    hm = HashMap()
    a = [5,100,231,3,4, 105]
    for i in a:
        hm.add(i,i)
    print(hm.get(5))
    print(hm.get(105))
    print(hm.get(100))
    print(hm.get(231))
