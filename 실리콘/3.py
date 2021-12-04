from collections import deque

def isSame(wave, deq):
  answer = True
  for i in range(len(wave)):
    if wave[i] != deq[i]:
      return False
  return True

def hasRepeat(wave):
  len_wave = len(wave)
  deq = deque(wave)

  for i in range(1, len_wave):
    deq.rotate(1)
    if isSame(wave, deq):
      return i
  
  return len_wave

def add_wave(wave1, wave2):
  new_wave = [0]*len(wave1)
  for i in range(len(wave1)):
    new_wave[i] = wave1[i] + wave2[i]
  return new_wave

def isConst(wave):
  first = wave[0]
  for i in range(len(wave)):
    if wave[i] != first:
      return False
  return True

def cal_wave(wave):
  value = 0
  if isConst(wave):
    return value
  
  for w in wave:
    value += (w*w)
  return value
  
def solution(wave1, wave2):
    answer = int(1e9)
    len1, len2 = len(wave1), len(wave2)
    wave1, wave2 = deque(wave1), deque(wave2)
    
    if len1 < len2:
      wave1, wave2 = wave2, wave1
      len1, len2 = len2, len1
    
    new_wave2 = deque([0]*len1)
    for i in range(len1):
      new_wave2[i] = wave2[i % len2]
    
    for i in range(len(wave2)):
      result = add_wave(wave1, new_wave2)
      leng = hasRepeat(result)
      if leng < len(result):
        value = cal_wave(result[:leng+1])
      value = cal_wave(result)
      if value < answer:
        answer = value
      new_wave2.rotate(1)
    
    return answer
      
sol1 = solution([1,2,2,1,1,2], 	[-2,-1])
sol2 = solution([2,-1,3], [-1,-1])
sol3 = solution([0,1,1,1,1,1], [0,0,1,0,0,0])
sol4 = solution([2,0,1,1,1,0], [0,0,-1])

print(sol1) #2
print(sol2) #9
print(sol3) #0
print(sol4) #1