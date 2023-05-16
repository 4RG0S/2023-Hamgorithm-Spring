# Python3로 채점시 시간초과남, pypy3로 채점시 통과
import sys

def floydWarshall(distance, V):
    for k in range(1, V + 1):
        for i in range(1, V + 1):
            for j in range(1, V + 1):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    distance = [[sys.maxsize] * (V + 1) for _ in range(V + 1)]
    
    for _ in range(E):
        a, b, cost = map(int, sys.stdin.readline().split())
        distance[a][b] = cost
    
    floydWarshall(distance, V)
    
    answer = sys.maxsize
    
    for i in range(1, V + 1):
        answer = min(answer, distance[i][i])
        
    if answer == sys.maxsize:
        print(-1)
    else:
        print(answer)