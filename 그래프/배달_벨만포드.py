INF = int(1e9)

def bf(N, road):
  dist = [INF for _ in range(N)]
  dist[0] = 0
  
  for i in range(N-1):
    for r in road:
      prev, curr, cost = r[0]-1, r[1]-1, r[2]
      if dist[prev] != INF and dist[curr] > dist[prev] + cost:
        dist[curr] = dist[prev] + cost
      if dist[curr] != INF and dist[prev] > dist[curr] + cost:
        dist[prev] = dist[curr] + cost
      
  return dist
  
def solution(N, road, K):
    answer = 0
    
    routes = bf(N, road)
    for cost in routes:
      if cost <= K:
        answer += 1
  
    return answer

N = 5
K = 3
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
sol = solution(N, road, K)
print(sol) #4