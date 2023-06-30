import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

graph = [list(map(int, input().rstrip())) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def check(y, x):
    return 0 <= y < n and 0 <= x < n

estate = []

def dfs(y, x):
    count = 0
    global graph
    global estate
    queue = deque()
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        count += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if check(ny, nx):
                if graph[ny][nx] == 1:
                    queue.append((ny,nx))
                    graph[ny][nx] = 0
    estate.append(count)

# 모든 위치에 방문하여 1인 경우 dfs 함수를 실행해 단지 개수를 세도록 함
for y in range(n):
    for x in range(n):
        if graph[y][x] == 1:
            graph[y][x] = 0
            dfs(y, x)
print(len(estate))
estate.sort()
# for 문으로 안쓰고 한 줄로 출력하고 싶어서 join함수를 사용함
print('\n'.join(map(str,estate)))

