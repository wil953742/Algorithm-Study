import copy

def makeBlock(size, number):
    newBlock = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(number)
        newBlock.append(row)
    return newBlock

def rotate(block):
    size = len(block)
    newBlock = makeBlock(size, 0)
    
    for i in range(size):
        for j in range(size):
            newBlock[j][size-i-1] = block[i][j]
    
    return newBlock
    
def isSolved(block):
    for row in block:
        for element in row:
            if element != 1:
                return False
    return True

def matching(key, lock, transI, transJ):
    size = len(key)
    newLock = copy.deepcopy(lock)
    for i in range(size):
        for j in range(size):
            if i+transI >= 0 and j+transJ >= 0 and i+transI < len(newLock) and j+transJ < len(newLock):
                newLock[i+transI][j+transJ] = newLock[i+transI][j+transJ] + key[i][j]
    return newLock

def test(key, lock):
    keySize = len(key)
    lockSize = len(lock)
    for transI in range(-(keySize-1), lockSize+1):
        for transJ in range(-(keySize-1), lockSize+1):
            result = matching(key, lock, transI, transJ)
            if isSolved(result):
                return True
    return False

def solution(key, lock):
    size = len(key)
    for i in range(4):
        key = rotate(key)
        result = test(key, lock)
        if result:
            return True
    return False

key = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sol = solution(key, lock)
print(sol)
