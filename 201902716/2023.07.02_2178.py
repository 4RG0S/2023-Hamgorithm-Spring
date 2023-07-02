def bfs(miro, N, M):
    queue = [(0, 0)] # 시작칸 추가
    dist = [[0] * M for _ in range(N)] # 미로 각 위치별 거리 리스트 초기값 0
    dist[0][0] = 1 # 시작칸 거리 1로 설정
    
    # queue에 갈 수 있는 칸이 있는 경우 반복
    while queue:
        x, y = queue.pop(0) # 현재 칸
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]: # 4 방향
            nx, ny = x + dx, y + dy
            
            # 미로를 벗어나거나, 미로가 막혀있으면 건너뛰기
            if nx < 0 or nx >= N or ny < 0 or ny >= M or miro[nx][ny] == 0:
                continue
            
            # 거리 설정이 안된 경우
            if dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1 # 다음위치 거리 = 현재위치 거리 + 1
                queue.append((nx, ny)) # 다음위치 추가
                
    return dist[N - 1][M - 1]

def main():
    N, M = map(int, input().split())
    miro = []
    
    # 미로 입력받기
    for _ in range(N):
        miro.append(list(map(int, input())))
                    
    print(bfs(miro, N, M))

if __name__ == '__main__':
    main()
