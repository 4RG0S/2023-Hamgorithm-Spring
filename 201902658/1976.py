n = int(input())
m = int(input())
connections = [list(map(int, input().split())) for _ in range(n)]
parents = list(range(n))
travel_plan = list(map(int, input().split()))

# 루트 노드 찾기
def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]

# 두 노드를 하나의 집합으로 합치기
def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        if root1 > root2:
            parents[root1] = root2
        else:
            parents[root2] = root1

# 그래프에 기반하여 연결 정보 처리
for i in range(n):
    for j in range(n):
        if connections[i][j] == 1:
            union(i, j)

# 여행 계획 내 도시들이 모두 연결되어 있는지 확인
ans = "YES"
base_root = find(travel_plan[0] - 1)
for city in travel_plan[1:]:
    if find(city - 1) != base_root:
        ans = "NO"
        break

print(ans)