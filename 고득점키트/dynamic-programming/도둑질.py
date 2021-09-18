def solution(money):
    numOfHouse = len(money)
    newMoney = money.copy()
    temp = []
    for i in range(numOfHouse):
        if(i%2==0):
            temp.append(0)
        else:
            temp.append(1)
    total = []
    for i in range(numOfHouse):
        sum = 0
        for j in range(numOfHouse):
            sum += newMoney[j]*temp[j]
        total.append(sum)
        last = newMoney.pop()
        newMoney.insert(0, last)

    return max(total)

money = [1,2,3,1,2,3,1,2]
sol = solution(money)
print(sol)