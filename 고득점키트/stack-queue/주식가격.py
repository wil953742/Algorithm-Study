from collections import deque 

def solution(prices):
  answer = []
  deq = deque(prices)
  while deq:
    target = deq.popleft()

    count = 0
    for i in deq:
      if target > i:
        count += 1
        break
      count += 1
    
    answer.append(count)

  return answer

print(solution([1,2,3,2,3]))