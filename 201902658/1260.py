def depth_first_search(node):
    print(node, end=' ')  # 현재 노드 출력
    visited[node] = True  # 현재 노드 방문 처리
    for i in range(1, vertex_count + 1):
        if not visited[i] and adjacency_matrix[node][i]:  # 방문하지 않았고, 인접한 노드일 경우
            depth_first_search(i)  # DFS 수행

def breadth_first_search(node):
    queue = [node]  # BFS를 위한 큐
    visited[node] = False  # 현재 노드 방문 처리
    while queue:
        node = queue.pop(0)  # 큐에서 노드를 하나씩 꺼냄
        print(node, end=' ')  # 현재 노드 출력
        for i in range(1, vertex_count + 1):
            if visited[i] and adjacency_matrix[node][i]:  # 방문하지 않았고, 인접한 노드일 경우
                queue.append(i)  # 큐에 추가
                visited[i] = False  # 노드 방문 처리

import sys

vertex_count, edge_count, start_vertex = map(int, sys.stdin.readline().split())  # 입력 받기
adjacency_matrix = [[0] * (vertex_count + 1) for _ in range(vertex_count + 1)]  # 인접 행렬 초기화
visited = [False for _ in range(vertex_count + 1)]  # 방문 리스트 초기화

for _ in range(edge_count):  # 간선 정보 입력 받기
    vertex_a, vertex_b = map(int, sys.stdin.readline().split())
    adjacency_matrix[vertex_a][vertex_b] = 1
    adjacency_matrix[vertex_b][vertex_a] = 1

depth_first_search(start_vertex)  # DFS 수행
print()
breadth_first_search(start_vertex)  # BFS 수행
