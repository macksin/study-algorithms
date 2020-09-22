def urlfy(w):
    end = True
    new_word = list()
    for n in w[::-1]:
        if n == ' ':
            continue
        elif (end == True):
            end = False
        elif n == ' ':
            new_word.append('02%')
        else:
            new_word.append(n)
    return ''.join(new_word[::-1])

if __name__ == "__main__":
    
    word = input()

    print(urlfy(word))