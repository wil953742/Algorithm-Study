import math

def solution(progresses, speeds):
    answer = []
    stack = []
    costs = [math.ceil((100-p)/s) for p,s in zip(progresses, speeds)]
    now = costs[0]
    for i in range(len(costs)):

        if len(stack)!=0 and now < costs[i]:
            answer.append(len(stack))
            stack = [costs[i]]
            now = costs[i]
        else :
            stack.append(costs[i])
    
    if len(stack) != 0 :
        answer.append(len(stack))

    return answer

sol = solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
print(sol)

sol2 = solution([93, 30, 55], [1, 30, 5])
print(sol2)