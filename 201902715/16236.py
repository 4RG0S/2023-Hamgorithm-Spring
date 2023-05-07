from typing import List
import sys
from heapq import heappush, heappop


"""
아기상어 위치로부터 상-좌-우-하 순서로 bfs 돌리기?
    - 잡아먹을 수 있는 위치가 나오면
        - 잡아먹기 -> 해당위치 0으로 변경
        - exp증가
        - exp == level이면 level증가 및 exp 초기화
        - 해당 위치에서 bfs시작
    - 계속 돌아도 안 나오면
        - bfs가 다시시작되지 않으므로, 자동 종료
    - LRUD 순서로 문제가 생겼는데 왜그럴까?
"""

baby_shark_level = 2
baby_shark_exp = 0
move = 0


def bfs(space_map: List[List[int]], start_i, start_j):
    global baby_shark_level
    global baby_shark_exp
    global move

    시작점으로부터의_최단거리 = [
        [sys.maxsize for _ in range(len(space_map))] for _ in range(len(space_map))
    ]
    시작점으로부터의_최단거리[start_i][start_j] = 0
    
    heap = []

    queue = [(start_i, start_j)]
    while queue:
        i, j = queue.pop(0)

        for ii, jj in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
            if not (0 <= ii < len(space_map) and 0 <= jj < len(space_map)):
                continue

            if space_map[ii][jj] > baby_shark_level:
                continue

            if 시작점으로부터의_최단거리[ii][jj] <= 시작점으로부터의_최단거리[i][j] + 1:
                continue

            시작점으로부터의_최단거리[ii][jj] = 시작점으로부터의_최단거리[i][j] + 1
            queue.append((ii, jj))

            if 0 < space_map[ii][jj] < baby_shark_level:
                heappush(heap, (시작점으로부터의_최단거리[ii][jj], ii, jj))

    if len(heap) == 0:
        return

    r, ii, jj = heappop(heap)
    move += r
    baby_shark_exp += 1
    if baby_shark_level == baby_shark_exp:
        baby_shark_level += 1
        baby_shark_exp = 0
    space_map[ii][jj] = 0
    bfs(space_map, ii, jj)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    space_map = []
    baby_shark_coord = (-1, -1)
    for i in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        try:
            baby_shark_coord = (i, line.index(9))
        except ValueError:
            pass
        space_map.append(line)

    space_map[baby_shark_coord[0]][baby_shark_coord[1]] = 0
    bfs(space_map, baby_shark_coord[0], baby_shark_coord[1])
    print(move)
