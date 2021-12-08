import heapq
from collections import defaultdict

def abstract(s, i):
  count = 1
  current = ""
  start = 0
  answer = ""
  
  while start+i <= len(s):
    current = s[start: start+i]
    start += i
    
    if s[start: start+i] == current:
      count += 1
      continue
    else :
      if count > 1:
        answer += str(count)
        
      answer += current
      count = 1

  answer += s[start:]
  
  return len(answer)
  

def solution(s):
  answer = []
  
  for i in range(1, len(s)+1):
    heapq.heappush(answer, abstract(s, i))
  
  return heapq.heappop(answer)

sol1 = solution("aabbaccc")
sol2 = solution("ababcdcdababcdcd")
sol3 = solution("abcabcabcabcdededededede")
sol4 = solution("xababcdcdababcdcd")

print(sol1)
print(sol2)
print(sol3)
print(sol4)