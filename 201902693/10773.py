import sys
input = sys.stdin.readline
n = int(input())
result = []
for _ in range(n) :
    a = int(input())
    if a == 0 :
        result.pop()
    else :
        result.append(a)

print(sum(result))