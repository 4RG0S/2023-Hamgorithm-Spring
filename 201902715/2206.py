'''
### DFS로 위 방법 구현 했더니 안되는데, BFS로 해보자

나의 생각 순서
1. dfs에서 visited를 관리하는 부분이 비효율적이었다.
2. 그럼 visited 없이 (0, 0)에서 특정 위치까지의 거리를 기록하겠다는 생각으로 접근했다.
	- 생각할점
		- (벽을 부수지 않고 도달할 수 있는 최단 거리, 벽을 부수고 도달할 수 있는 최단 거리) 튜플로 관리
		- 특정 위치에 벽을 부수지 않고 온 게 더 잘 한 것이다. 
		   벽을 부수지 않고 도달할 수 있는 최단거리 >= 벽을 부수고 도달할 수 있는 최단 거리 라는 관계가 생김
		   벽을 부수지 않고 3,3까지 3의 거리로 갔으면서, 벽을 부수고는 3,3까지 4의 거리로 간다하면 비효율적인 벽부수기가 발생한 것이니 무시해버리는 것임
3. 이래도 오류가 나서 BFS로 수정해서 풀이 완료
'''


import sys
from typing import List, Tuple
from collections import deque


N: int
M: int
matrix: List[List[int]]
queue: deque[Tuple[int, int]]
# ((0, 0)으로부터 벽을 부수지 않고 최단 거리, 벽을 부수고 최단 거리)
distances: List[List[Tuple[int, int]]]

FAILED_DISTANCE = 999999999
DEBUG = False


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, sys.stdin.readline().strip())))
    
    START = (0, 0)
    END = (N - 1, M - 1)
    
    distances = [[(FAILED_DISTANCE, FAILED_DISTANCE) for _ in range(M)] for _ in range(N)]
    distances[START[0]][START[1]] = (1, 1)
    queue = deque([START])
    while queue:
        i, j = queue.popleft()
        for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if not (0 <= ii < N and 0 <= jj < M):
                continue
            
            if DEBUG:
                print()
                print(f"-----{ii, jj}-----")
                for r in distances:
                    print(r)
            
            if matrix[ii][jj] == 0: # 벽이 아닌 경우
                if distances[i][j][0] + 1 < distances[ii][jj][0]:
                    distances[ii][jj] = (distances[i][j][0] + 1, distances[ii][jj][1])
                    queue.append((ii, jj))
                if distances[i][j][1] + 1 < distances[ii][jj][1]:
                    distances[ii][jj] = (distances[ii][jj][0], distances[i][j][1] + 1)
                    queue.append((ii, jj))
            else:
                if distances[i][j][0] + 1 < distances[ii][jj][1]:
                    distances[ii][jj] = (distances[ii][jj][0], distances[i][j][0] + 1)
                    queue.append((ii, jj))
            
            distances[ii][jj] = (distances[ii][jj][0], min(distances[ii][jj]))

    answer = min(distances[END[0]][END[1]])
    print (answer if answer != FAILED_DISTANCE else -1)
