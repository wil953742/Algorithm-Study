

def solution(triangle):
    height = len(triangle)
    list = [0]*height    
    for i in range(height):
        if i==0:
            list[0] = triangle[i]
            continue
        xList = list[i-1]
        temp = []
        for j in range(i+1):
            left = 0
            right = 0
            if(j-1>=0):
                left = xList[j-1] + triangle[i][j]
            
            if(j<len(xList)):
                right = xList[j] + triangle[i][j]
            if(left>right):
                temp.append(left)
            else:
                temp.append(right)
        list[i] = temp

    return max(list[height-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
sol = solution(triangle)
print(sol)