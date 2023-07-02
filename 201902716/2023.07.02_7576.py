from collections import deque

def bfs(farm, N, M):
    queue = deque()
    days = -1 # 이미 다 익은 상태에도 하루 +1 하므로 초기값 -1

    # 익은 토마토 찾아 queue에 넣기
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                queue.append((i, j))

    # 토마토 익히기
    while queue:
        # 오늘 익은 토마토 개수 만큼 반복
        for _ in range(len(queue)):
            x, y = queue.popleft() # 나는야 익은 토마토
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]: # 4 방향 다 익혀주마
                nx, ny = x + dx, y + dy
                
                # 농장 안에 있는 안익은 토마토면
                if 0 <= nx < N and 0 <= ny < M and farm[nx][ny] == 0:
                    farm[nx][ny] = 1 # 익히기
                    queue.append((nx, ny))
                
        days += 1
        
    # 안 익은 토마토 있으면 -1
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 0:
                return -1
                   
    return days

def main():
    M, N = map(int, input().split())
    farm = []
    
    # 토마토 농장 입력받기
    for _ in range(N):
        farm.append(list(map(int, input().split())))
                    
    print(bfs(farm, N, M))

if __name__ == '__main__':
    main()
