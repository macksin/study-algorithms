from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func took: {:2.8f} sec'.format(te-ts))
        return result
    return wrap

# Does a string contains only unique characters?

# Bruteforce implementation
@timing
def isRepeated_bruteFoce(word):
    for i1 in range(len(word)):
        for i2 in range(len(word)):
            if (i1 == i2):
                continue
            elif (word[i1] == word[i2]):
                return True
    return False

# Hashtable implementation with a method
# that returns duplicates of the same key

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
                
    def show(self):
        print(self.table)

@timing
def isRepetead(word, wordHash):
    for w in word:
        if len(wordHash.get_duplications(w)) > 1:
            return True
    return False


if __name__ == "__main__":

    word = input()

    print(isRepeated_bruteFoce(word))

    hashtable = HashTable(word)
    for i, w in enumerate(word):
        hashtable.add(w, i)

    print(isRepetead(word, hashtable))