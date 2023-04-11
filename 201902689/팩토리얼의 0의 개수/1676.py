import math
num = int(input())

result = 0
fact = list(str(math.factorial(num)))

while fact:
    tmp = fact.pop()
    if tmp == "0":
        result += 1
    else:
        break

print(result)
