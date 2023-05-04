# 위상 정렬
import sys

from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
inDegree = [0 for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    inDegree[b] += 1
    graph[a].append(b)

queue = deque()
ans = []

for i in range(1, n + 1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    current = queue.popleft()
    ans.append(current)

    for x in graph[current]:
        inDegree[x] -= 1

        if inDegree[x] == 0:
            queue.append(x)

print(*ans, end=" ")