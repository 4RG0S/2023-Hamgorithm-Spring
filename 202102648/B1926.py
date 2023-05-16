import sys
sys.setrecursionlimit(10**6)
from collections import deque 
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

lst = []

visited = [[False] * m for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] != True:
            visited[i][j] = True
            q.append((j, i))
            cnt = 1

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = dx[k] + x
                    ny = dy[k] + y
                    if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] != True and graph[ny][nx] != 0:
                        visited[ny][nx] = True
                        cnt += 1
                        q.append((nx, ny))

            else:
                lst.append(cnt)  


if len(lst) != 0:
    print(len(lst))
    print(max(lst))
else:
    print(0)
    print(0)


