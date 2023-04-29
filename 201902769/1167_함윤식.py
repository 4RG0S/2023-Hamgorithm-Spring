import sys
import collections
import queue

def dfs(start):
    distance = [sys.maxsize for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]
    distance[start] = 0
    
    pq = queue.PriorityQueue()
    pq.put([0, start])

    while not pq.empty():
        cur_distance, cur_node = pq.get()
        if visited[cur_node]:
            continue
        else:
            visited[cur_node] = 1
        
        for next_node, next_distance in edges[cur_node]:
            if cur_distance + next_distance < distance[next_node]:
                distance[next_node] = cur_distance + next_distance
                pq.put([distance[next_node], next_node])
    # print(distance.index(max(distance[1:])), distance[distance.index(max(distance[1:]))], visited, edges)
    return distance.index(max(distance[1:])), distance[distance.index(max(distance[1:]))]
    

v = int(input())
edges = collections.defaultdict(list)

for j in range(1,v+1):
    arr = list(map(int, input().split()))

    for i in range(1,len(arr)-1,2):
        edges[arr[0]].append([arr[i], arr[i+1]])

first, _ = dfs(1)
second, _ = dfs(first)
_, result = dfs(second)
print(result)