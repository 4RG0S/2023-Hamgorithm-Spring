n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = []

# 2차원 배열에 서로 어떤 게 연결 돼있는 지 저장
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# dfs 함수 만들기
def dfs(check, num):
    num += 1
    visited[check] = True

    if check == b:
        result.append(num)

    for i in graph[check]: #방문 안한 리스트 원소들 반복문으로 돌면서 방문유무 체크
        if not visited[i]: #아직 방분 안한 노드일 경우 dfs돌리기
            dfs(i, num)

dfs(a, 0)
if len(result) == 0: #친척관계가 없을 경우
    print(-1)
else: #친척 관계가 있을 경우
    print(result[0]-1)