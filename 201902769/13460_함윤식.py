import queue
n, m = map(int, input().split())
board = []
R = (0,0)
B = (0,0)
O = (0,0)
dy, dx = [0,0,1,-1], [1,-1,0,0]

for i in range(n):
    board.append([i for i in input()])

#R B O 좌표 기록
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            R = (i,j)
        if board[i][j] == 'B':
            B = (i,j)
        if board[i][j] == 'O':
            O = (i,j)

#특정 방향으로 벽이 아닌 경우 계속 이동
def move(x, y, d): 
    flag = False

    while board[x+dx[d]][y+dy[d]] != '#' and 0<=x+dx[d]<n and 0<=y+dy[d]<m:
        x, y = x+dx[d], y+dy[d]

        if board[x][y] == 'O':
            flag = True
            

    return ((x, y), flag)

def dfs():
    q = queue.Queue()
    q.put((R,B,1))

    while not q.empty():
        cur_R, cur_B, life = q.get()
        
        if life == 11:
            return -1
        
        for i in range(4):
            next_R, rFlag = move(cur_R[0], cur_R[1], i)
            next_B, bFlag = move(cur_B[0], cur_B[1], i)

            if bFlag:
                continue
            if rFlag:
                return life
            
            if next_R == next_B:
                wei = tuple(map(abs, (next_R[0] - cur_R[0], next_R[1] - cur_R[1]))) > tuple(map(abs, (next_B[0] - cur_B[0], next_B[1] - cur_B[1])))

                if wei:
                    next_R = (next_R[0]-dx[i], next_R[1]-dy[i])
                else:
                    next_B = (next_B[0]-dx[i], next_B[1]-dy[i])
            
            q.put((next_R, next_B, life + 1))

print(dfs())
# queue에 이전 R, B의 위치 정보를 queue에 기록해 이전 위치 정보를 기준으로 이동할 모든 경로를 탐색
# dfs로 모든 경우의 수를 탐색해 최소 시간을 리턴함