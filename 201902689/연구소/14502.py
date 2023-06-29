# 1. 벽을 세울 수 있는 모든 경우의 수를 구한다.
# 2. 벽을 세운다.
# 3. 바이러스를 퍼트린다.
# 4. 안전 영역의 크기를 구한다.

from collections import deque
import copy
import sys
input = sys.stdin.readline
from itertools import combinations
n, m = map(int, input().split(' '))

graph = [list(map(int, input().split(' '))) for _ in range(n)]
'''
    dy, dx 테크닉
    for 문을 4번 돌면서 각각 아래, 위, 왼쪽, 오른쪽을 탐색할 수 있음
'''
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

result = 0
# 코드를 쉽게 볼 수 있도록 그래프의 이동 범위 체크 로직을 함수로 뺌
def check(y, x):
    return 0 <= y < n and 0 <= x < m

def bfs():
    test_graph = copy.deepcopy(graph)

    queue = deque()
    for i in range(n):
        for j in range(m):
            if test_graph[i][j] == 2:
                queue.append((i, j))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if check(ny, nx):
                if test_graph[ny][nx] == 0:
                    test_graph[ny][nx] = 2
                    if (ny, nx) not in queue:
                        queue.append((ny, nx))

    count = 0
    global result
    for i in range(n):
        count += test_graph[i].count(0)
    result = max(result, count)

# 백트래킹을 사용하여 벽을 세울 수 있는 모든 경우에 대해 탐색한다.
def making_wall(count):
    if count == 3:
        bfs()
        return
    else:
        spaces = []
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    making_wall(count+1)
                    # 나왔을 때 다시 초기화해주어 백트래킹이 되도록 한다
                    graph[i][j] = 0

making_wall(0)
print(result)