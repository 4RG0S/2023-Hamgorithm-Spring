import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

lst = [list(map(int, input().split())) for _ in range(n)]   # 상자

q = deque()

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:  # 1인 값만 queue에 추가
            q.append([i, j])

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):      # 현재 좌표 기준 4방향으로 확인
            nx = dx[i]+x
            ny = dy[i]+y
            
            if 0<=nx<n and 0<=ny <m and lst[nx][ny]==0: # 범위에 맞게 탐색
                lst[nx][ny] = lst[x][y]+1       # 날짜 +1
                q.append([nx, ny])


bfs()
ans=0
for i in range(n):
    for j in range(m):
        if lst[i][j]==0:
            print(-1)
            exit(0)
        ans = max(ans, lst[i][j])   # 최대 날짜 구하기

print(ans-1)