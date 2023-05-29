import numpy as np
n= int(input())
nums = list(map(int, input().split(" ")))

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(np.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

count = 0
for num in nums:
    if isPrime(num):
        count += 1

print(count)