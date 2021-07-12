def solution(array, commands):
    answer = []
    
    for command in commands:
        i,j,k = command
        
        sub_array = sorted(array[i-1 : j])
        
        answer.append(sub_array[k-1])    
        
    return answer
