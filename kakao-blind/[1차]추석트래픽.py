def transform(time):
    hour, minute, second = time.split(':')
    hour = int(hour) * 60 * 60 * 1000
    minute = int(minute) * 60 * 1000
    second = int(float(second) * 1000)

    return hour + minute + second

def solution(lines):
    new_lines = []
    max_value = 0

    for line in lines:
        date, time, cost = line.split(' ')
        new_cost = int(float(cost[:-1]) * 1000) - 1
        new_time = transform(time)
        
        new_lines.append([new_time - new_cost, new_time])
        
    for time1, time2 in new_lines:
        time1_s, time1_l = time1, time1 + 999
        time2_s, time2_l = time2, time2 + 999
        
        cnt = 0
        for start, last in new_lines:
            if last >= time1_s and start <= time1_l:
                cnt += 1
        if cnt > max_value:
            max_value = cnt
        
        cnt = 0
        for start, last in new_lines:
            if last >= time2_s and start <= time2_l:
                cnt += 1
        if cnt > max_value:
            max_value = cnt
    
    return max_value
    
sol = solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"])
print(sol) #7