list = [0,1,2,3,4,5,6,7,8]

def makeCombins(N):
    temp = []
    for i in range(1, N):
        temp.append([i, N-i])
    return temp

def calculation(temp, i, j):
    temp.append(i+j)
    if i-j > 0:
        temp.append(i-j)
    temp.append(i*j)
    if i%j == 0:
        temp.append(i//j)

def makeList(N, quantity):
    
    if(quantity==1):
        list[1] = [N]
        return [N]
    
    temp = []
    temp.append(getN(N, quantity))
    combins = makeCombins(quantity)
    for combin in combins:
        front = list[combin[0]]
        back = list[combin[1]]
        for i in front:
            for j in back:
                calculation(temp, i, j)

    list[quantity] = temp
    return temp

def getN(N, quantity):
    if(quantity==1):
        return N
    
    return getN(N*10+N%10, quantity-1)

def isPerfect(N, number):
    if number==0:
        return True
    (quotient, remainder) = divmod(number, 10)
    if remainder != N:
        return False
    return isPerfect(N, quotient)


def solution(N, number):
    for i in range(1,9):
        if number in makeList(N, i):
            return i
    
    return -1

sol1 = solution(5, 12)
sol2 = solution(2, 11)
print('Sol1 : ', sol1)
print('Sol2 : ', sol2)
