from collections import deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    current = (0, 0, 0)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 9:
                current = (i, j, 0)
                matrix[i][j] = 0
    
    size = 2
    size_count = 0
    count = 0
    while True:
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        visit = [[1] * n for _ in range(n)]
        visit[current[0]][current[1]] = 0
        que = deque([current])
        li = []
        while que:
            x, y, d = que.popleft()
            nd = d + 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and visit[nx][ny]:
                    if matrix[nx][ny] <= size:
                        que.append((nx, ny, nd))
                        visit[nx][ny] = 0
                        if 0 < matrix[nx][ny] < size:
                            li.append((nx, ny, nd))
        
        li = sorted(li, key=lambda x : (x[2], x[0], x[1]))
        if len(li) == 0:
            break
        
        nx, ny, nd = li[0]
        count += nd
        current = (nx, ny, 0)
        matrix[nx][ny] = 0
        
        size_count += 1
        if size == size_count:
            size += 1
            size_count = 0
    
    print(count)
    
if __name__ == '__main__':
    main()