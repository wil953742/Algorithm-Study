from collections import deque

def solution(rows, columns, connections, queries):
    answer = [0] * len(queries)
    deq = deque(connections)
    
    for l in range(len(queries)):
      x_s, y_s, x_e, y_e = queries[l]
      
      if x_s > x_e:
        x_e, x_s = x_s, x_e          
      
      if y_s > y_e:
        y_s, y_e = y_e, y_s
      
      for _ in range(len(deq)):
        connection = deq.popleft()
        isPutAgain = True
        x1, y1, x2, y2 = connection
        
        if x1 > x2:
          x1, x2 = x2, x1
        
        if y1 > y2:
          y1, y2 = y2, y1
             
        for i in range(x_s, x_e + 1):
          for j in range(y_s, y_e + 1):

            if (x1, y1) == (i, j) or (x2, y2) == (i, j):
              if x1 < x_s or x2 > x_e or y1 < y_s or y2 > y_e:
                answer[l] += 1
                isPutAgain = False
        
        if isPutAgain:
          deq.append(connection)
        

    return answer
  

sol1 = solution(4, 3, [[1,1,2,1],[1,2,1,3],[1,3,2,3],[2,2,2,3],[2,2,3,2],[2,3,3,3],[3,2,3,3],[3,2,4,2],[4,1,4,2]], [[2,2,3,1],[1,2,4,2]])
print(sol1)