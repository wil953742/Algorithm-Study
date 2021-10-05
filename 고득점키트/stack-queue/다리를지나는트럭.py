from collections import deque

def sumBridge(bridge_queue):
  if len(bridge_queue)==0:
    return 0
  
  return sum(list(map(lambda x:x[0], bridge_queue)))

def solution(bridge_length, weight, truck_weights):
  
  truck_queue = deque(truck_weights)
  bridge_queue = deque()
  time = 0

  while 1:

    if len(truck_queue)==0:
      if len(bridge_queue)==0:
        break
      else:
        time += 1
        if bridge_queue[0][1] == time:
          bridge_queue.popleft()
    
    else:
      time += 1

      if len(bridge_queue)==0:
        turn = truck_queue.popleft()
        bridge_queue.append([turn, time+bridge_length])
        continue
      
      if bridge_queue[0][1] == time:
        bridge_queue.popleft()

      if (sumBridge(bridge_queue) + truck_queue[0]) <= weight:
        turn = truck_queue.popleft()
        bridge_queue.append([turn, time+bridge_length])
        continue
      
      else:
        pass

  return time


sol = solution(10, 10, [7,4,5,6])
print(sol) #32