import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())

def primes(n1, n2):
    arr = [True] * (n2 + 1)
    arr[0] = False
    arr[1] = False
    
    for i in range(2, int(n2 ** 0.5) + 1):
        if arr[i]:
            for j in range(i * i, n2 + 1, i):
                arr[j] = False
    
    result = []
    for i in range(n1, n2+1):
        if arr[i]:
            result.append(i)
    
    # [i for i in range(n1, n2 + 1) if arr[i]]      17 ~ 19
    return result

lst = primes(n1, n2)
for val in lst:
    print(val)
