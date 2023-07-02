import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
tomato = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

queue = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:   # 처음에 익은 토마토 위치 append
            queue.append([i, j])


def bfs():
    while queue:
        # 처음 토마토 좌표 x, y
        x, y = queue.popleft()
        # 처음 토마토 주변 토마토들을 익힘
        for i in range(4):
            #dx, dy돌면서 주변 익힘
            next_x, next_y = dx[i] + x, dy[i] + y
            # 범위 넘어가지 않는지 체크
            if 0 <= next_x < n and 0 <= next_y < m and tomato[next_x][next_y] == 0:
                # 익히면 횟수 +1
                tomato[next_x][next_y] = tomato[x][y] + 1
                # 익은 토마토 위치 append (그 토마토 기준으로 주변 탐색)
                queue.append([next_x, next_y])

bfs()
for i in tomato:
    for j in i:
        # 다 돌아서 0인 게 있으면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    # 계속 돌면서 최댓값 갱신
    result = max(result, max(i))
print(result - 1)