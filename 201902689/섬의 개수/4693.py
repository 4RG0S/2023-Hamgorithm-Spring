from collections import deque
import sys
# 재귀 깊이 제한 늘려주어야함
sys.setrecursionlimit(10000)
# 8개 방향을 해야하므로 추가
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1 ,1, -1, 1, -1, 1]

def dfs(y, x):
    graph[y][x] = 0
    for i in range(8):
        ny, nx = y + dy[i], x + dx[i]
        if (0 <= ny < h) and (0 <= nx < w) and graph[ny][nx] == 1:
            dfs(ny, nx)

while True:
    w, h = map(int, input().split(' '))
    if h == w == 0: break
    graph = list(list(map(int, input().split(' '))) for _ in range(h))
    count = 0
    for row in range(h):
        for col in range(w):
            if graph[row][col] == 1:
                dfs(row, col)
                count += 1
    print(count)