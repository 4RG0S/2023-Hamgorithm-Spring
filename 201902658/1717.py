import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())


def union(node1, node2):
    root1 = find_root(node1)
    root2 = find_root(node2)

    # 두 노드의 루트가 같다면 이미 같은 집합에 속해 있다
    if root1 == root2:
        return

    # 아니라면 두 집합을 합친다
    parent[root1] = root2
    return


def find_root(node):
    # 노드가 자신의 부모라면, 그 노드는 루트이다
    if parent[node] == node:
        return node

    # 아니라면 루트를 재귀적으로 찾아서 경로 압축을 수행한다
    parent[node] = find_root(parent[node])
    return parent[node]


# 각 노드의 부모를 자기 자신으로 초기화한다
parent = [i for i in range(n + 1)]

for _ in range(m):
    operation, nodeA, nodeB = map(int, input().split())

    # 합집합 연산
    if operation == 0:
        union(nodeA, nodeB)
    # 두 노드가 같은 집합에 속해 있는지 확인한다
    else:
        rootA = find_root(nodeA)
        rootB = find_root(nodeB)
        if rootA == rootB:
            print('YES')
        else:
            print('NO')
