from collections import deque

t = int(input())
next_x = [-1, 1, 0, 0]
next_y = [0, 0, 1, -1]

def bfs(x, y):
        bfs_stack.append([x, y])
        while bfs_stack:
            x, y = bfs_stack.popleft()
            table[x][y] = 2
            for i in range(4):
                nx = next_x[i] + x 
                ny = next_y[i] + y

                if (nx != -1 and nx < m) and (ny != -1 and ny < n) and table[nx][ny] == 1:
                    table[nx][ny] = 2
                    bfs_stack.append([nx, ny])

for p in range(t):
    m, n, k = map(int, input().split())
    table = [[0 for col in range(n)] for row in range(m)]
    bfs_stack = deque([])
    cnt = 1
    for _ in range(k):
        a, b = map(int, input().split())
        table[a][b] = 1

    for i in range(m):
        for j in range(n):
            if table[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt-1)