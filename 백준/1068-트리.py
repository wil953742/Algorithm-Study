
N = int(input())
li = list(map(int, input().split()))

class Node:
  def __init__(self, value):
    self.value = value
    self.parent = None
    self.children = []
  
  def addChild(self, child):
    self.children.append(child)

  def getChildren(self):
    return self.children

  def setParent(self, parent):
    self.parent = parent
  
  def getParent(self):
    return self.parent

  def removeChild(self, target):
    self.children.remove(target)

treeNodes = [Node(x) for x in range(N)]
head = treeNodes[0]

for i in range(len(li)):
  if li[i] < 0:
    continue

  treeNodes[i].setParent(treeNodes[li[i]])
  treeNodes[li[i]].addChild(treeNodes[i])

print(treeNodes);

targetNode = int(input())

if targetNode == 0:
  print(0)

else:  
  targetParent = treeNodes[targetNode].getParent()
  targetParent.removeChild(targetNode)


def dfs(node):
  answer = 0
  if len(node.getChildren())==0:
    return 1
  for child in node.getChildren():
    return answer + dfs(child)

print(dfs(head))
