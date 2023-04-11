import sys

def floydWarshall(distance, n):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    distance = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
       
    for i in range(1, n + 1):
        distance[i][i] = 0
         
    for _ in range(m):
        u, v, cost = map(int, input().split())
        distance[u][v] = min(cost, distance[u][v])
    
    floydWarshall(distance, n)
    
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if distance[a][b] == sys.maxsize:
                print("0", end=" ")
            else:
                print(distance[a][b], end=" ")
        print()