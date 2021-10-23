# num = int(input())

# bad = []
# for _ in range(num):
#   bad.append(list(map(int, input().split())));

def factorial(x):
  if x==1:
    return 1 
  return x * factorial(x-1)

x = 0



print(factorial(8) - x ) 