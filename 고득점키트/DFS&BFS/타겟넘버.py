from itertools import combinations


def solution(numbers, target):
  answer = 0
  for i in range(len(numbers)):
    combi = list(combinations(numbers, i))
    for com in combi:
      sumCombi = 0 if len(com)==0 else sum(com)
      sumNumbers = sum(numbers)-sumCombi
      sumTotal = sumNumbers - sumCombi
      if sumTotal==target:
        answer += 1      

  return answer



sol = solution([1, 1, 1, 1, 1], 3)
print(sol) #5