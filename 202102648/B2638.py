import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def fill():
    visited = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(False)
        visited.append(row)

    queue = [(0, 0)]
    visited[0][0] = True
    graph[0][0] = -1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if not visited[nx][ny] and graph[nx][ny] <= 0:
                    visited[nx][ny] = True
                    graph[nx][ny] = -1
                    queue.append((nx, ny))


def sol():
    for i in range(1, n-1):
        for j in range(1, m-1):
            if graph[i][j]==1:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if graph[nx][ny] == -1:
                        cnt+=1
                if cnt >= 2:
                    graph[i][j] = 0

def c1():
    for i in range(1, n-1):
        for j in range(1, m-1):
            if graph[i][j] == 1:
                return False
    return True

def c2():
    for i in range(1, n-1):
        for j in range(1, m-1):
            if graph[i][j] == 1:
                return True
    return False

ans=0

if c2():
    while True:
        fill()
        sol()
        ans += 1
        if c1():
            break

print(ans)