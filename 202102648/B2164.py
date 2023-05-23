from collections import deque
import sys
input = sys.stdin.readline

q = deque([i+1 for i in range(int(input()))])

while (len(q) != 1):
    q.popleft()
    q.append(q.popleft())

print(*q)