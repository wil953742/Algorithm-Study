heap = [0, 0, 0]

def test(list):
  newList = list[:]
  newList[0] = 1
  
test(heap)

print(heap)