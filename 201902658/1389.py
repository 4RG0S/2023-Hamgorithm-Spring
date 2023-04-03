# 폴로이드 워셜 알고리즘
import sys

def floydwarshall(distance, V):
    result = []
    for i in range(1, V + 1):
        for a in range(1, V + 1):
            for b in range(1, V + 1):
                distance[a][b] = min(distance[a][b], distance[a][i] + distance[i][b])
        
    for i in distance[1 : ]:
        ans = 0
        for j in i:
            if j == sys.maxsize:
                continue
            else:
                ans += j
        result.append(ans)
    print(result.index(min(result)) + 1)


if __name__ == "__main__":
    V, E = map(int, input().split())
    distance = [[sys.maxsize for j in range(V + 1)] for i in range(V + 1)]
     
    for i in range(1, V + 1):
        distance[i][i] = 0
    for i in range(E):
        u, v = map(int, input().split())
        distance[u][v] = 1
        distance[v][u] = 1
    
    floydwarshall(distance, V)