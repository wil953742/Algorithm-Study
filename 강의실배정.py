inputList = [input() for _ in range(4)]
inputList.pop(0)
temp = [i.split() for i in inputList]
timeTable = [[int(x),int(y)] for x,y in temp]
timeTable.sort(key=lambda x:x[1])

answer = 0
std = 0
for i in timeTable:
    start = i[0]
    end = i[1]
    if std <= start:
        answer += 1
        std = end 
    else:
        pass

print(answer)

