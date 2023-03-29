import math

n = int(input())
fact = str(math.factorial(n))
result = 0
for i in range(len(fact)-1, 0, -1):
    if fact[i] == '0':
        result += 1
    else:
        break
print(result)
