import copy

def validCheck(board, block):
    new_board = copy.deepcopy(board)
    for b in block:
        if board[b[0]][b[1]] != 0:
            return False
        new_board[b[0]][b[1]] = 1
    
    for b in block:
        if b[0]+1<len(board) and new_board[b[0]+1][b[1]] == 0:
            return False
        if b[1]+1<len(board) and new_board[b[0]][b[1]+1] == 0:
            return False
        if b[0]-1>=0 and new_board[b[0]-1][b[1]] == 0:
            return False
        if b[1]-1>=0 and new_board[b[0]][b[1]-1] == 0:
            return False
        
    return True

def rotate(board):
    new_board = [[0]*len(board) for _ in range(len(board[0]))]    
    for row in range(len(board)):
        for col in range(len(board[0])):
            new_board[col][len(board)-1-row] = board[row][col]
    return new_board

def getBlock(board, row, col, record):
    board[row][col] = 0
    record.append([row, col])
    
    if row+1<len(board) and board[row+1][col] == 1:
        getBlock(board, row+1, col, record)
    
    if col+1<len(board) and board[row][col+1] == 1:
        getBlock(board, row, col+1, record)
    
    if row-1>=0 and board[row-1][col] == 1:
        getBlock(board, row-1, col, record)
    
    if col-1>=0 and board[row][col-1] == 1:
        getBlock(board, row, col-1, record)

    return record


def getBlockList(board):
    block_list = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                record = getBlock(board, row, col, [])
                block_list.append(record)
                
    return block_list

def mvCheck(board, block):
    size = len(board)
    init_size = len(block)
    while 1:
        if validCheck(board, block):
            for i in block:
                board[i[0]][i[1]] = 1
                print(block)
            return True     
            
        block = [[b[0], b[1]+1] for b in block if b[1]+1 < size]
        if len(block) != init_size:
            break

    while 1:
        if validCheck(board, block):
            for i in block:
                board[i[0]][i[1]] = 1
                print(block)
            return True      
            
        block = [[x+1, y] for x, y in block if x+1 < size]
        if len(block) != init_size:
            break

    while 1:
        if validCheck(board, block):
            for i in block:
                board[i[0]][i[1]] = 1
                print(block)
            return True      
            
        block = [[x, y-1] for x, y in block if y-1 >= 0]
        if len(block) != init_size:
            break
    
    while 1:
        if validCheck(board, block):
            for i in block:
                game_board[i[0]][i[1]] = 1
                print(block)
            return True      
            
        block = [[x-1, y] for x, y in block if x-1 >= 0]
        if len(block) != init_size:
            break
    
    return False

def solution(game_board, table):
    answer = 0
    block_list = getBlockList(table)
    for block in block_list:
        test_block = block
        for i in range(4):
            test_block = rotate(test_block)
            if mvCheck(game_board, test_block):
                answer += 1
                break

    return answer

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
sol = solution(game_board, table)
print(sol) #14
