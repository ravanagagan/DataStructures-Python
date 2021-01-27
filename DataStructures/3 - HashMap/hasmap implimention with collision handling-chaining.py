# get_hash login we will implement the same in hash_table class

# def get_hash(key):
#     h = 0
#     for char in key:
#         h += ord(char)
#     return h % 100


class HashTable:
    def __init__(self):
        self.MAX_SIZE = 100
        self.arr = [[] for i in range(self.MAX_SIZE)]

    def get_hash(self, key):
        chars = 0
        for char in key:
            chars += ord(char)
        return chars % self.MAX_SIZE

    # instead of this h.add('march 6', 130) we can use h['march 6'] = 130 by replacing add with __setitem__
    # what we are doing is operator overriding
    # replace 'def add(self, key):' this with 'def __setitem__(self, key)'
    def __setitem__(self, key, val):
        hash_data = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[hash_data]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash_data][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[hash_data].append((key, val))

    # instead of this h.add('march 6', 130) we can use h['march 6'] = 130 by replacing add with __setitem__
    # what we are doing is operator overriding
    # replace 'def get(self, key):' this with 'def __getitem__(self, key)'
    def __getitem__(self, key):
        hash_data = self.get_hash(key)
        for element in self.arr[hash_data]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        hash_data = self.get_hash(key)
        for index, element in enumerate(self.arr[hash_data]):
            if element[0] == key:
                del self.arr[hash_data][index]


if __name__ == '__main__':
    h = HashTable()
    h.get_hash('march 6')
    # h.add('march 6', 130)
    # print(h.get('march 6'))
    h['march 6'] = 130
    h['march 6'] = 50
    h['march 7'] = 140
    h['march 8'] = 150
    h['march 17'] = 200
    print(h.arr, end="\n")
    print(h['march 6'])
    print(h['march 17'])
    del h['march 17']
    print(h.arr)
