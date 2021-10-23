num = int(input())

schedules = []
for _ in range(num):
  schedules.append(list(map(int, input().split())))

calendar = {}
for schedule in schedules:
  for i in range(schedule[0], schedule[1]+1):
    if calendar.get[i]:
      calendar[i] += 1
    else:
      pass