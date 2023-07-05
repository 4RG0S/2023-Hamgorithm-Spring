'''
### 각 보드 상태에서 LRUB로 이동하는 케이스 모두 테스트

중복을 줄이기 위해, 빨간 구슬이 도달한 위치가 같으면 탐색 X
문제 크기가 작아서, 나이브하게 풀림
'''
import sys
from typing import List, Tuple
from enum import Enum
from collections import deque


N: int = -1
M: int = -1
board: List[List[str]] = []
red_pos: Tuple[int, int] = tuple()
blue_pos: Tuple[int, int] = tuple()
hole_pos: Tuple[int, int] = tuple()
red_blue_visited: List[List[List[List[bool]]]] = []
WRONG_ANSWER = 10000


class GameState(Enum):
    RED_IN_HOLE = 0
    BLUE_IN_HOLE = 1
    CONTINUE = 2
    STUCK = 3


def move(
    red_pos: Tuple[int, int],
    blue_pos: Tuple[int, int],
    di: int,
    dj: int,
) -> Tuple[Tuple[int, int], Tuple[int, int], GameState]:
    red_i, red_j = red_pos
    blue_i, blue_j = blue_pos
    
    red_i += di
    red_j += dj
    blue_i += di
    blue_j += dj
    
    new_red_pos = (red_i, red_j)
    new_blue_pos = (blue_i, blue_j)
    
    if board[new_red_pos[0]][new_red_pos[1]] == "#":
        new_red_pos = red_pos
    if board[new_blue_pos[0]][new_blue_pos[1]] == "#":
        new_blue_pos = blue_pos
    
    if new_red_pos == new_blue_pos:
        new_red_pos = red_pos
        new_blue_pos = blue_pos
    
    game_state: GameState = GameState.CONTINUE
    if red_pos == new_red_pos and blue_pos == new_blue_pos:
        game_state = GameState.STUCK
    else:
        if new_red_pos == hole_pos:
            new_red_pos = (-1, -1)
            game_state = GameState.RED_IN_HOLE
        if new_blue_pos == hole_pos:
            new_blue_pos = (-1, -1)
            game_state = GameState.BLUE_IN_HOLE

    return new_red_pos, new_blue_pos, game_state


def move_until_stuck(
    red_pos: Tuple[int, int],
    blue_pos: Tuple[int, int],
    di: int,
    dj: int,
) -> Tuple[Tuple[int, int], Tuple[int, int], GameState]:
    new_red_pos = (red_pos[0], red_pos[1])
    new_blue_pos = (blue_pos[0], blue_pos[1])
    
    red_in_hole = False
    blue_in_hole = False
    
    game_state = None
    while game_state != GameState.STUCK:
        new_red_pos, new_blue_pos, game_state = move(new_red_pos, new_blue_pos, di, dj)
        if game_state == GameState.RED_IN_HOLE:
            red_in_hole = True
        elif game_state == GameState.BLUE_IN_HOLE:
            blue_in_hole = True
    
    if blue_in_hole:
        return new_red_pos, new_blue_pos, GameState.BLUE_IN_HOLE
    if red_in_hole:
        return new_red_pos, new_blue_pos, GameState.RED_IN_HOLE

    return new_red_pos, new_blue_pos, GameState.CONTINUE


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    for i in range(N):
        board_row = []
        for j, elem in enumerate(sys.stdin.readline().strip()):
            if elem == "R":
                red_pos = (i, j)
                elem = "."
            elif elem == "B":
                blue_pos = (i, j)
                elem = "."
            elif elem == "O":
                hole_pos = (i, j)

            board_row.append(elem)
        board.append(board_row)
    
    red_blue_visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
    red_blue_visited[red_pos[0]][red_pos[1]][blue_pos[0]][blue_pos[1]] = True
    
    queue = deque([])
    queue.append((red_pos, blue_pos, 0))
    answers = [WRONG_ANSWER]
    while queue:
        red_pos, blue_pos, trial = queue.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_red_pos, new_blue_pos, state = move_until_stuck(red_pos, blue_pos, di, dj)
            # print((di, dj))
            # print(f"{(red_pos, blue_pos)} -> ", end="")
            # print((new_red_pos, new_blue_pos))
            # print()
            if state == GameState.RED_IN_HOLE:
                answers.append(trial + 1)
            if state == GameState.BLUE_IN_HOLE:
                continue
            if trial + 1 >= 10:
                continue
            if red_blue_visited[new_red_pos[0]][new_red_pos[1]][new_blue_pos[0]][new_blue_pos[1]]:
                continue
            red_blue_visited[new_red_pos[0]][new_red_pos[1]][new_blue_pos[0]][new_blue_pos[1]] = True
            queue.append((new_red_pos, new_blue_pos, trial + 1))
    
    answer = min(answers)
    print(answer if answer != WRONG_ANSWER else -1)
