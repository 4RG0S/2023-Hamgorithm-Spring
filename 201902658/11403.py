import sys

def floydWarshall(distance, N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if distance[i][j] == 1 or (distance[i][k] == 1 and distance[k][j]):
                    distance[i][j] = 1

if __name__ == "__main__":
    N = int(input())
    distance = []
    
    for i in range(N):
        distance.append(list(map(int, input().split())))
    
    floydWarshall(distance, N)
    
    for a in range(N):
        for b in range(N):
            print(distance[a][b], end=" ")
        print()