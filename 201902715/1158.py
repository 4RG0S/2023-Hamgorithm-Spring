import sys

N, K = map(int, sys.stdin.readline().split())

arr = [i + 1 for i in range(N)]

solution = []
idx = 0
while len(arr) > 0:
    idx = (idx + K - 1) % len(arr)
    elem = arr.pop(idx)
    solution.append(elem)

print('<', end='')
for e in solution[:-1]:
    print(e, end=', ')
print(solution[-1], end='>')
