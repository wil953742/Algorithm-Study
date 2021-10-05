import collections 

def solution(priorities, location):
  queue = [(i,p) for i,p in enumerate(priorities)]
  deq = collections.deque(queue)
  result = []
  while len(deq)>0:
    turn = deq.popleft()
    if any(turn[1] < q[1] for q in deq):
      deq.append(turn)
    else:
      result.append(turn)      

  answer = 1
  for i in range(len(result)):
    if result[i][0] == location:
      answer += i
      break
  
  return answer

sol = solution([1, 1, 9, 1, 1, 1], 0)
print(sol)