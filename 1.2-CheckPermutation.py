from functools import wraps
from time import time

# My idea is checking the permutation via keychecking letters in words

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func took: {:2.8f} sec'.format(te-ts))
        return result
    return wrap


class HashTable:
    
    def __init__(self, array):
        self.size = len(array)
        self.table = [[] for i in range(self.size)]
        
    def hashing(self, keyvalue):
        return hash(keyvalue) % self.size

    def add(self, keyvalue, value):
        self.table[self.hashing(keyvalue)].append((keyvalue, value))
        
    def get(self, element):
        l = self.table[self.hashing(element)]
        if len(l) == 1:
            return l[0][1]
        else:
            for i in l:
                if element == i[0]:
                    return i[1]
                
    def get_duplications(self, element):
        dups = []
        l = self.table[self.hashing(element)]
        if len(l) == 1:
            return [l[0]]
        else:
            for i in l:
                if element == i[0]:
                    dups.append(i)
            return dups

    def get_duplications_keys(self, element):
        dups = []
        l = self.table[self.hashing(element)]
        if len(l) == 1:
            return [l[0]]
        else:
            for i in l:
                if element == i[0]:
                    dups.append(i)
            return dups
        
    def __iter__(self):
        return iter(self.table)
                
    def show(self):
        print(self.table)

@timing
def checkPermutation(word1hash, word2hash):
    for x, y in zip(word1hash, word2hash):
        print(x, y, x == y)
        if (sorted(x) != sorted(y)):
            return False
    return True

@timing
def checkPermutationSimple(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    return False

if __name__ == "__main__":
    
    word1 = input()
    print('\n')
    word2 = input()
    print('\n')

    
    hash1 = HashTable(word1)
    for i, w in enumerate(word1):
        hash1.add(w, w)

    hash2 = HashTable(word2)
    for i, w in enumerate(word2):
        hash2.add(w, w)

    hash1.show()
    print("*******")
    hash2.show()

    print(checkPermutation(hash1, hash2))

    print(checkPermutationSimple(hash1, hash2))