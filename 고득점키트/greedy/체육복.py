def solution(n, lost, reserve):
    reserve.sort()
    students = [1]*n

    for l in lost:
        students[l-1] = 0
    
    new_reserve = []
    for r in reserve:
        if students[r-1]==0:
            students[r-1] = 1
        else:
            new_reserve.append(r)

    for r in new_reserve:
        if r-2>=0 and students[r-2]==0:
            students[r-2] = 1
        elif r<len(students) and students[r]==0:
            students[r] = 1

    return sum(students)

sol1 = solution(5, [2,4], [5])
print(sol1)
# sol2 = solution(5, [2,4], [3])
# sol3 = solution(3, [3], [1])
# sol4 = solution(14, [1,3,5,7,9,11,13], [2,4,6,8,10,14])
