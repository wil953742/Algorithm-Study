#error 존재ㅜㅜㅜ
def solution(number, k, start=0):
    if((len(number)-1-start)==k):
        max_value = max(list(number[start:]))
        return number[:start] + max_value

    front = list(number[start:start+k+1])
    max_value = max(front)
    max_index = front.index(max_value)
    
    if max_index==0:
        return solution(number, k, start+1)
    else:
        k-=max_index
        number = number[:start] + number[start+max_index:]
        if k<=0 :
            return number
        
        return solution(number, k ,start)

sol = solution("1991", 1)
print(sol) #"775841"
