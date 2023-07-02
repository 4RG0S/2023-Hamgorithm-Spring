import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

def dfs(i): 
    global cnt
    #탐색함수
    cnt=cnt+1
    visit[i-1]=cnt
    nod[i-1].sort()
    for v in nod[i-1]:
        if  visit[v-1]==0:
            dfs(v)
cnt=0
x, y, z = map(int, input().split())
#입력 간선 시작
visit=[0]*(x)
#방문전 false 설정
nod=[[] for k in range(x)]
for o in range(y):
    i,j = map(int, input().split())
    nod[i-1].append(j)
    nod[j-1].append(i)
#간선 추가
dfs(z)

for i in range(x):
    print(visit[i])