words = { "zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}

def transform(s, word):
    new_word = ""
    l = len(word)
    i = 0
    
    while i < len(s) :
        if s[i:i+l] == word:    
            new_word += str(words[word])
            i += l
        else:
            new_word += s[i]
            i += 1

    return new_word


def solution(s):
    
    for word in words.keys():
        print(s)
        s = transform(s, word)
    
    return int(s)

sol = solution("one4seveneight")
print(sol)