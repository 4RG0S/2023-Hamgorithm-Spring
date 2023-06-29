import queue

def dfs(graph, start, visited):
    visited[start] = True   # visited 리스트에 start의 방문을 기록
    result = [start]
    for i in graph[start]:
        if i not in visited:
            result += dfs(graph, i, visited)
    return result

def bfs(graph, root):
    result = []
    vertex_queue = queue.Queue()    # 정점을 저장할 큐 선언
    visited = [False] * (max(graph.keys()) + 1) # visited를 리스트로 구현
    vertex_queue.put(root)
    visited[root] = True

    while not vertex_queue.empty():
        vertex = vertex_queue.get()
        result.append(vertex)
        if vertex not in graph:
            continue
        for neighbor in graph[vertex]:  # 인접 노드를 순
            if not visited[neighbor]:
                vertex_queue.put(neighbor)
                visited[neighbor] = True

    return result

def main():
    number_of_vertex, number_of_edge, start_vertex = map(int, input().split())

    graph = {}

    for i in range(number_of_edge):
        vertex_first, vertex_second = map(int, input().split())
        if vertex_first not in graph:
            graph[vertex_first] = [vertex_second]
        else:
            graph[vertex_first].append(vertex_second)

        if vertex_second not in graph:
            graph[vertex_second] = [vertex_first]
        else:
            graph[vertex_second].append(vertex_first)

    visited = {}
    result_of_dfs = dfs(graph, start_vertex, visited)
    result_of_bfs = bfs(graph, start_vertex)

    print(*result_of_dfs)
    print(*result_of_bfs)

if __name__ == "__main__":
    main()
