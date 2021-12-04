def solution(names, homes, grades):
  answer = [0]*len(names)
  
  dict = []
  for i in range(len(names)):
    x, y = homes[i]
    dist = (x*x) + (y*y)
    num = grades[i] // 1

    dict.append([names[i], dist, num, i])
  
  dict.sort(key=lambda x: (-x[2], -x[1], x[0]))
  
  for i in range(len(names)):
    answer[dict[i][3]] = i+1
  
  return answer
  
sol = solution(["azad","andy","louis","will","edward"], [[3,4],[-1,5],[-4,4],[3,4],[-5,0]], [4.19, 3.77, 4.41, 3.65, 3.58])
print(sol) #[2, 3, 1, 5, 4]