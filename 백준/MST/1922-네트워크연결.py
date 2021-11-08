numOfComputer = int(input())
numOfEdge = int(input())
edgeList = [list(map(int, input().split())) for _ in range(numOfEdge)]
edgeList.sort(key = lambda x: x[2])

parent = {}
for i in range(1, numOfComputer+1):
  parent[i] = i

def find(node):
  if parent[node] == node:
    return node
  else:
    return find(parent[node])

def union(node1, node2):
  a, b = find(node1), find(node2)
  parent[a] = b

mst = []

for i in edgeList:
  if find(i[0]) != find(i[1]):
    mst.append(i[2])
    union(i[0], i[1])
  
  if len(mst) == (numOfComputer-1):
    break

print(sum(mst))