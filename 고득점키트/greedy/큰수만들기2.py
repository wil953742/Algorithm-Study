def solution(number, k):
    stack = []
    for i in range(len(number)):
        curr = number[i]
        while 1:
            if len(stack)==0:
                stack.append(curr)
                break

            prev = stack.pop()
            
            if curr > prev :
                k -= 1

            else :
                stack.append(prev)
                stack.append(curr)
                break

            if k == 0:
                return ''.join(stack)+number[i:]
        
    if k>0:
        return ''.join(stack[:-k])
        

sol = solution("5674321", 4)
print(sol)