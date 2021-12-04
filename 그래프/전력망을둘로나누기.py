def dfs(graph, start, visited):
  visited[start] = 1
  
  for node in range(len(graph[start])):
    if graph[start][node]==1 and visited[node] == 0:
      dfs(graph, node, visited)
  
  return visited

def solution(n, wires):
    
  graph = [[0]*(n+1) for _ in range(n+1)]
  answer = n
  
  for start, last in wires:
    graph[start][last] = 1
    graph[last][start] = 1
   
  for start, last in wires:
    graph[start][last] = 0
    graph[last][start] = 0
    
    visited = dfs(graph, start, [0]*(n+1))
    print(visited)
    candidate = abs(n - sum(visited) * 2) 
    if candidate < answer:
      answer = candidate
    
    graph[start][last] = 1
    graph[last][start] = 1
  
  return answer
  
sol = solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
sol2 = solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])

print(sol)