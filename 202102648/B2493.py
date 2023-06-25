import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
lst = list(map(int, input().split()))

ans = [0] * n

s = deque()

for i in range(n):
    while s:
        if s[-1][0] > lst[i]:
            ans[i] = s[-1][1]+1
            break
        else:
            s.pop()
    s.append((lst[i], i))
    # print("i", i, "s", s)

print(*ans)