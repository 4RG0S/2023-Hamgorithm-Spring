import math
n = int(input())
for i in range(1,9) :
    if n > 10**i:
        if (n / (10**i)) - 0.5 >= (n // (10**i)) :
            n = math.ceil(n / (10**i)) * (10**i)
        else :
            n = math.floor(n / (10**i)) * (10**i)
print(n)