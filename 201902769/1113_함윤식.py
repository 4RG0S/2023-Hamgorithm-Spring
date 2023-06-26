import collections
n, m = map(int, input().split())
pool = []
for i in range(n):
    pool.append([int(i) for i in input()])

visit = collections.defaultdict(lambda:collections.defaultdict(int))
dy, dx = [0,0,1,-1], [1,-1,0,0]
count = 0

def bfs(height, x, y):
    
    global count
    cur_count = 1
    stack = [(x, y)]
    visit[x][y] = height
    
    # 주변이 벽으로 막혀 있는지
    flag = True
    
    
    # stack이 빌때까지 반복
    while stack:
        cur_x, cur_y = stack.pop()
        for i in range(4): # dydx를 이용해 사방위 탐색
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            
            # 방문한 경우
            if visit[next_x][next_y] == height:
                continue
            
            # 범위 안일 경우
            if 0 <= next_x < n and 0 <= next_y < m:
                if pool[next_x][next_y] < height:
                    cur_count += 1
                    
                    # height 보다 작으면서 외곽인 경우
                    if next_x == 0 or next_y == 0 or next_x == n-1 or next_y == m-1:
                        flag = False
                        
                    stack.append((next_x, next_y))
                    visit[next_x][next_y] = height
                    
    if flag:
        count += cur_count
                

# 수면의 높이를 1씩 높이며 체크
for height in range(2, 10):
    for x in range(1,n-1):
        for y in range(1,m-1):
            if visit[x][y] == height or pool[x][y] >= height:
                continue
            else:
                bfs(height, x, y)
    
print(count)