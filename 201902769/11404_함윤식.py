import sys
n = int(input())
m = int(input())

distance = [[sys.maxsize for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    distance[a-1][b-1] = min(distance[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
  
for i in range(n):
    for j in range(n):
        if distance[i][j] == sys.maxsize:
            distance[i][j] = 0
            
for i in distance:
    print(*i)