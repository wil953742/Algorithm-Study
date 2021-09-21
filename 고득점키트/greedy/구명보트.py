def solution(people, limit):
    people.sort()
    i, j, boat = 0, len(people)-1, 0
    while j>=i:
        boat+=1
        if people[i]+people[j] <= limit:
            i+=1
            j-=1
        else:
            j-=1

    return boat

sol = solution([70, 80, 50], 100)
print(sol)
