n = [1,2,3,4]
r = 3

permutation = []
result = [0] * r
visited = [False] * len(n)

def dfs(n, r, l):
  if l == r:
    permutation.append(result[:])
  else:
    for i in range(len(n)):
      if not visited[i]:
        result[l] = n[i]
        visited[i] = True
        dfs(n, r, l+1)
        visited[i] = False

dfs(n, r, 0)
print(permutation)
