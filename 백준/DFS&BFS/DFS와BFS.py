from collections import deque, defaultdict

graph = defaultdict(list)

n, m, v = list(map(int,input().split(' ')))

for _ in range(m):
  s, l = list(map(int, input().split(' ')))
  graph[s].append(l)
  graph[l].append(s)

# dfs
dfs_visited = []

def dfs(s, graph):
  dfs_visited.append(s)
  
  for i in sorted(graph[s]):
    if i not in dfs_visited:
      dfs(i, graph)

dfs(v, graph)

print(' '.join(map(str,dfs_visited)))

# bfs
bfs_visited = []

def bfs(s, graph):
  queue = deque([s])
  
  while len(queue) > 0:
    target = queue.popleft()    
    if target not in bfs_visited:
      bfs_visited.append(target)
      queue.extend(sorted(graph[target]))
  
bfs(v, graph)

print(' '.join(map(str, bfs_visited)))