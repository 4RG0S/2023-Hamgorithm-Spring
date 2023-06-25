import heapq
import sys
input = sys.stdin.readline
Inf = float("inf")

def main():
    count = 0
    while True:
        count += 1
        
        n = int(input())
        if n == 0: break

        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
            
        dist = [[Inf for j in range(n)] for i in range(n)]
        dist[0][0] = matrix[0][0]

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        que = [(dist[0][0], 0, 0)]
        while que:
            d, x, y = heapq.heappop(que)
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] > d + matrix[nx][ny]:
                    dist[nx][ny] = d + matrix[nx][ny]
                    heapq.heappush(que, (dist[nx][ny], nx, ny))
    
        print(f'Problem {count}: {dist[n-1][n-1]}')
    
if __name__ == "__main__":
    main()