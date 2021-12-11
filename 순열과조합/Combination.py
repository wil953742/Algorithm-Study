n = [ 1, 2, 3, 4 ]
r = 2

result = [0] * r
combination = []

def dfs(l, s, n, r):
  if l == r:
    combination.append(result[:])
  else:
    for i in range(s, len(n)):
      result[l] = n[i]
      dfs(l+1, i+1, n, r)
  
dfs(0, 0, n, r)
print(combination)