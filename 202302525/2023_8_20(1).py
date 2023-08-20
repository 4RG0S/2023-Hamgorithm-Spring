import sys

input = sys.stdin.readline

n = int(input())
result = {}

for _ in range(n):
    a, b = input().split()
    
    if b == 'enter':
        result[a] = 1

    else:
        del result[a]

print(*sorted(result.keys(), reverse=True), sep='\n')