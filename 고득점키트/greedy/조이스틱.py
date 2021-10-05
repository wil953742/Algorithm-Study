panix = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, \
    'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

def solution(name):
    location = []
    rev_location = []
    zig_zag_location = []
    total = 0
    for i in range(len(name)):
        if(name[i] != 'A'):
            seq = panix[name[i]]
            total += min(seq-1, 27-seq)
            location.append(i)
            rev_location.append(len(name)-i)
    
    for i in range(len(location)-1):
        temp = 0
        temp += location[i]*2
        temp += max(rev_location[i+1:])
        
        zig_zag_location.append(temp)

    total += min(max(location), max(rev_location), min(zig_zag_location))

    print(location)
    print(rev_location)
    return total

sol2 = solution("ABABAAAAAAABA")
print(sol2)