# Since I will user built-in functions of Python
# I will build, from scratch some simple algorithms

# In this case the fastest way to reverse a string in
# python is [::-1] but I will implement the fastest I know
# complexity : O(n/2) In-Place String reversal

def inPlaceReverse(w):
    l = len(w)
    w1 = list(w)
    for i in range(l//2):
        tmp = w1[i]
        w1[i] = w1[l-i-1]
        w1[l-i-1] = tmp
    return ''.join(w1)

if __name__ == "__main__":
    
    word = input()

    print(inPlaceReverse(word))