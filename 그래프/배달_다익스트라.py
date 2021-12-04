import heapq
from collections import defaultdict
from collections import deque
# sort, sorted
# list의 shallow copy 와 deep copy
# set 자료 구조

# +a로 영상으로 올릴 부분 : 각종 알고리즘 
# 1. union-find 를 이용한 MST (Prim 개념 + Kruskal 알고리즘 실전), 
# 2. 그래프 최단경로 ( Bellman-Ford, Dijkstra 알고리즘 실전 및 차이, 플로이드-마샬(예정))

# CSS 높이와 넓이 속성, Position 속성,,,? 정도

INF = int(1e9)

def dijkstra(start, graph, dists):
  heap = []
  dists[1] = 0
  heapq.heappush(heap, (0, start))
  
  while heap:
    dist, node = heapq.heappop(heap)
    if dists[node] < dist:
      continue
        
    for next, cost in graph[node]:
      
      if dists[next] > dist + cost:
        dists[next] = dist + cost
        heapq.heappush(heap, (dist+cost, next))
  
  return dists

def solution(N, road, K):
  dist = [INF] * (N+1)
  graph = defaultdict(list)

  for a,b,c in road:
    graph[a].append([b, c])
    graph[b].append([a, c])  
  
  print(graph)
  routes = dijkstra(1, graph, dist)
  print(routes)
  answer = 0
  for cost in routes:
    if cost <= K:
      answer += 1

  return answer

N = 5
K = 3
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,3],[5,3,1],[5,4,2],[2,4,1]]
sol = solution(N, road, K)
print(sol) #4