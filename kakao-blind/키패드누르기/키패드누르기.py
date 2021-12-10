keyboard = { '1': [0, 3], '2': [1,3], '3':[2,3], '4': [0,2], '5': [1,2], '6': [2,2], '7': [0,1], '8': [1,1], '9':[2,1], '*': [0,0], '0':[1,0], '#':[2,0]}

def distance(coor1, coor2):
  return abs(coor1[0] - coor2[0]) + abs(coor1[1] - coor2[1])

def solution(numbers, hand):
    answer = ''
    left_thumb = keyboard['*']
    right_thumb = keyboard['#']
    
    for i in numbers:
      key = keyboard[str(i)]

      if i == 0 or i % 3 == 2:
        left_dis = distance(left_thumb, key)
        right_dis = distance(right_thumb, key)
        
        if left_dis > right_dis:
          answer += 'R'
          right_thumb = key
        
        elif right_dis > left_dis:
          answer += 'L'
          left_thumb = key
        
        else:
          if hand=="right":
            answer += 'R'
            right_thumb = key
          
          else:
            answer += 'L'
            left_thumb = key
        
      elif i % 3 == 1:
        answer += 'L'
        left_thumb = key
      else:
        answer += 'R'
        right_thumb = key
    
    return answer
  
sol1 = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
sol2 = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
print(sol1)
print(sol2)