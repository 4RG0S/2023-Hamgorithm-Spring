from collections import deque
from typing import List
import sys

def find_maximum_flow(num_nodes: int, graph: List[List[int]], capacity: List[List[int]], flow: List[List[int]]) -> int:
    result = 0
    while True:
        q = deque([1])
        previous = [-1] * (num_nodes + 1)
        previous[1] = 0

        while q:
            current = q.popleft()
            for next_node in graph[current]:
                if capacity[current][next_node] - flow[current][next_node] > 0 and previous[next_node] == -1:
                    previous[next_node] = current
                    q.append(next_node)
                    if next_node == num_nodes:
                        break
        
        if previous[num_nodes] == -1:
            break

        current_flow = sys.maxsize
        i = num_nodes
        while i != 1:
            current_flow = min(current_flow, capacity[previous[i]][i] - flow[previous[i]][i])
            i = previous[i]

        i = num_nodes
        while i != 1:
            capacity[previous[i]][i] -= current_flow
            capacity[i][previous[i]] += current_flow
            i = previous[i]

        result += current_flow

    return result


def main():
    num_tests = int(input())
    for _ in range(num_tests):
        num_nodes, num_edges = map(int, input().split())
        graph = [list() for _ in range(num_nodes + 1)]
        capacity = [[0] * (num_nodes + 1) for _ in range(num_nodes + 1)]
        flow = [[0] * (num_nodes + 1) for _ in range(num_nodes + 1)]

        for _ in range(num_edges):
            start, end = map(int, input().split())
            if start == 1 or end == num_nodes:
                capacity[start][end] = 1
            else:
                capacity[start][end] = sys.maxsize
            
            graph[start].append(end)
            graph[end].append(start)

        print(find_maximum_flow(num_nodes, graph, capacity, flow))

        for i in range(1, num_nodes + 1):
            graph[i].clear()

if __name__ == "__main__":
    main()
