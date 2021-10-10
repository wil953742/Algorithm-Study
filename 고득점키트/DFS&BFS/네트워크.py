def solution(n, computers):
    answer = 0

    def dfs(i, j, visited):
      computers[i][j] = 0
      if i+1 > n:
        return 1
      for newI in range(i+1, n):
        if computers[newI][i] == 1:
          visited.append()
          return dfs(newI, i, computers, visited)
      

    for i in range(n):
      for j in range(i):
        if computers[i][j]==1:
          visited = []
          dfs(i, j, computers, visited)

    return answer