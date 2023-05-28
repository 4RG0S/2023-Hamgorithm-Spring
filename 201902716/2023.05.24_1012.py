def bfs(field, M, N, x, y):
    queue = [(x, y)]
    field[y][x] = 0
    
    while queue:
        x, y = queue.pop(0)

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if field[ny][nx] == 1:
                queue.append((nx, ny))
                field[ny][nx] = 0

def main():
    T = int(input())
    for _ in range(T):
        M, N, K = map(int,input().split())
        baechu_field = [[0] * M for _ in range(N)]
        white_earthworm = 0
        
        for _ in range(K):
            x, y = map(int, input().split())
            baechu_field[y][x] = 1
        
        for y in range(N):
            for x in range(M):
                if baechu_field[y][x] == 1:
                    bfs(baechu_field, M, N, x, y)
                    white_earthworm += 1
                    
        print(white_earthworm)

if __name__ == '__main__':
    main()
