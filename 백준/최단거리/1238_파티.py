N, M, X = list(map(int, input().split(' ')))

INF = int(1e9)
d_0 = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
  start, end, time = list(map(int, input().split(' ')))
  d_0[start][end] = time

for k in range(1, len(d_0)):
  for i in range(1, len(d_0)):
    for j in range(1, len(d_0)):
      direct = d_0[i][j]
      trans = d_0[i][k] + d_0[k][j]
      
      if trans < direct:
        d_0[i][j] = trans

answer = 0      
for i in range(1, N+1):
  value = d_0[X][i] + d_0[i][X]
  if answer < value:
    answer = value
  
print(answer)