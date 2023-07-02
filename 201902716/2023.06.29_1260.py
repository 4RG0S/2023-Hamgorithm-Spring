def dfs(graph, s):
    visited = [] # 방문한 노드 순서 리스트
    stack = []
    stack.append(s) # stack에 시작노드 추가
    
    # stack에 노드가 있는 경우 반복
    while stack:
        n = stack.pop() # 방문할 노드
        
        # 방문하지 않은 노드인 경우
        if n not in visited:
            visited.append(n) # 방문한 노드 추가
            stack.extend(graph[n]) # 방문노드와 연결된 노드 추가
            
    return visited

def bfs(graph, s): 
    visited = [] # 방문한 노드 순서 리스트
    queue = []
    queue.append(s) # queue에 시작노드 추가
    
    # queue에 노드가 있는 경우 반복
    while queue:
        n = queue.pop(0) # 방문할 노드
        
        # 방문하지 않은 노드인 경우
        if n not in visited:
            visited.append(n) # 방문노드 추가
            queue.extend(graph[n]) # 방문노드와 연결된 노드 추가
          
    return visited

def main():
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    
    # 그래프 만들기
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    # dfs, stack에서 작은노드 부터 방문할 수 있게 정렬
    for n in graph:
        n.sort(reverse=True)
    print(*dfs(graph, V))
    
    # bfs, queue에서 작은노드 부터 방문할 수 있게 정렬
    for n in graph:
        n.sort()
    print(*bfs(graph, V)) 

if __name__ == '__main__':
    main()
