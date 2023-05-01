from collections import deque

col, row = map(int, input().split())
tomato_farm = [list(map(int, input().split())) for _ in range(row)]
dx = [-1, 1, 0, 0] # 상하좌우 탐색
dy = [0, 0, -1, 1]
ripe = deque([])
result = 0

for i in range(row): # 익은 토마토 위치 찾기
    for j in range(col):
        if tomato_farm[i][j] == 1:
            ripe.append([i,j])

def BFS(): # 인접한 토마토 탐색 위해 BFS 사용
    while ripe:
        x, y = ripe.popleft() # 출발점
        for i in range(4): # 상하좌우 탐색
            curx = dx[i] + x
            cury = dy[i] + y
            if 0 <= curx < row and 0 <= cury < col and tomato_farm[curx][cury] == 0:
                tomato_farm[curx][cury] = tomato_farm[x][y] + 1
                ripe.append([curx, cury])
                
BFS()
for i in tomato_farm:
    for j in i:
        if j == 0: 
            print(-1)
            exit(0)
    result = max(result, max(i))
    
print(result-1)
