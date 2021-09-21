def solution(m, n, puddles):
    distance = m+n-1
    list=[0]*distance
    for i in range(distance):
        if i==0 :
            list[0]=[[1,1]]
            continue
        temp=[]
        for coor in list[i-1]:
            if(coor[0]+1<=m):
                if([coor[0]+1,coor[1]] not in puddles):
                    temp.append([coor[0]+1,coor[1]])
            if(coor[1]+1<=n):
                if([coor[0],coor[1]+1] not in puddles):
                    temp.append([coor[0],coor[1]+1])
        list[i]=temp
    
    return len(list[distance-1])

sol = solution(4, 3, [[2,2]]);
print(sol); #4