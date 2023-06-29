from collections import deque

N, M, V = map(int,input().split()) # N은 정점의 개수, M은 간선의 개수, V는 시작점

zm = [[0] * (N+1) for i in range(N+1)] # (N+1)^2개의 2차원 영행렬 생성(간선을 표현하기 위해)

for i in range(M) : # 간선의 개수만큼 반복문
    a,b = map(int,input().split())
    zm[a][b] = zm[b][a] = 1 # 간선이 양방향이므로 둘다 1로 표현

visit_DFS = [0] * (N+1)
visit_BFS = [0] * (N+1) # 0은 사용하지 않으므로 N+1칸의 리스트 생성(영행렬도 같은 이유)
def DFS(d) : # 재귀를 이용한 깊이우선탐색
    visit_DFS[d] = 1 # 방문한 곳 체크
    print(d, end = ' ')
    for i in range(1,N+1) :
        if visit_DFS[i] == 0 and zm[d][i] == 1 : # 만약 visit_DFS가 0이면 아직 방문한 적이 없는것인데 zm[d][i] 또는 zm[i][d]가 1이라면 V와 i가 인접한 것이므로
            DFS(i)                               # DFS(i)를 실행시켜 재귀


def BFS(b) : # 큐를 이용한 넓이우선탐색
    q = deque([b]) # 큐 생성
    visit_BFS[b] = 1 # 처음 방문한 곳 체크

    while q : # 큐에 데이터가 없을 때까지
        b = q.popleft() # 이미 방문한 곳의 데이터 제거
        print(b, end = ' ') 
        for i in range(1, N+1) :
            if visit_BFS[i] == 0 and zm[i][b] == 1 : #DFS와 같은 원리로
                q.append(i)                          #큐에 다음 방문할 곳을 추가
                visit_BFS[i] = 1 # 방문한 곳 체크
DFS(V)
print()
BFS(V)