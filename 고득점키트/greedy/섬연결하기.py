def solution(n, costs):
    
    answer = 0

    def find(c):
        if par[c] == c:
            return c
        else:
            return find(par[c])

    def union(a, b):
        a, b = find(a), find(b)
        par[a] = b

    par = [i for i in range(n)]

    costs.sort(key = lambda x: x[2])
    for i in costs:
        if find(i[0]) != find(i[1]):
            answer += i[2]
            union(i[0], i[1])
        
    return answer

sol = solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
print(sol) #4