from collections import deque

m, n = map(int, input().split())
box = []
bfs_stack = deque([])
res = 0
next_x, next_y = [1,-1,0,0], [0,0,-1,1]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 1:
            bfs_stack.append([i, j])
    box.append(line)
    
while bfs_stack:
    x, y = bfs_stack.popleft()

    for i in range(4):
        nx = next_x[i] + x 
        ny = next_y[i] + y

        if (nx != -1 and nx < n) and (ny != -1 and ny < m) and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            bfs_stack.append([nx, ny])
        

for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit()
        res = max(res, j)

print(res-1)