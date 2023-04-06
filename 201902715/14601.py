import sys

# sys.setrecursionlimit(10 ** 8)


current_tile_id = 1
tile_map: list[list[int]]


def solve(start_i, start_j, end_i, end_j, drain_i, drain_j):
    global current_tile_id, tile_map

    if end_i - start_i == 2 and end_j - start_j == 2:
        for i in range(start_i, end_i):
            for j in range(start_j, end_j):
                if i == drain_i and j == drain_j:
                    continue
                tile_map[i][j] = current_tile_id
        current_tile_id += 1
        return

    mid_i = (start_i + end_i) // 2
    mid_j = (start_j + end_j) // 2

    """ mid_i, mid_j
    [ ] [ ] [ ] [ ]
    [ ] [ ] [ ] [ ]
    [ ] [ ] [x] [ ]
    [ ] [ ] [ ] [ ]
    """

    if drain_i < mid_i:
        if drain_j < mid_j:
            tile_map[mid_i][mid_j] = current_tile_id
            tile_map[mid_i - 1][mid_j] = current_tile_id
            tile_map[mid_i][mid_j - 1] = current_tile_id
            current_tile_id += 1

            solve(start_i, start_j, mid_i, mid_j, drain_i, drain_j)
            solve(start_i, mid_j, mid_i, end_j, mid_i - 1, mid_j)
            solve(mid_i, start_j, end_i, mid_j, mid_i, mid_j - 1)
            solve(mid_i, mid_j, end_i, end_j, mid_i, mid_j)
        else:
            tile_map[mid_i][mid_j] = current_tile_id
            tile_map[mid_i][mid_j - 1] = current_tile_id
            tile_map[mid_i - 1][mid_j - 1] = current_tile_id
            current_tile_id += 1

            solve(start_i, start_j, mid_i, mid_j, mid_i - 1, mid_j - 1)
            solve(start_i, mid_j, mid_i, end_j, drain_i, drain_j)
            solve(mid_i, start_j, end_i, mid_j, mid_i, mid_j - 1)
            solve(mid_i, mid_j, end_i, end_j, mid_i, mid_j)
    else:
        if drain_j < mid_j:
            tile_map[mid_i][mid_j] = current_tile_id
            tile_map[mid_i - 1][mid_j] = current_tile_id
            tile_map[mid_i - 1][mid_j - 1] = current_tile_id
            current_tile_id += 1

            solve(start_i, start_j, mid_i, mid_j, mid_i - 1, mid_j - 1)
            solve(start_i, mid_j, mid_i, end_j, mid_i - 1, mid_j)
            solve(mid_i, start_j, end_i, mid_j, drain_i, drain_j)
            solve(mid_i, mid_j, end_i, end_j, mid_i, mid_j)
        else:
            tile_map[mid_i - 1][mid_j] = current_tile_id
            tile_map[mid_i][mid_j - 1] = current_tile_id
            tile_map[mid_i - 1][mid_j - 1] = current_tile_id
            current_tile_id += 1

            solve(start_i, start_j, mid_i, mid_j, mid_i - 1, mid_j - 1)
            solve(start_i, mid_j, mid_i, end_j, mid_i - 1, mid_j)
            solve(mid_i, start_j, end_i, mid_j, mid_i, mid_j - 1)
            solve(mid_i, mid_j, end_i, end_j, drain_i, drain_j)


if __name__ == "__main__":
    K = int(sys.stdin.readline())
    side_size = 2**K
    x, y = map(int, sys.stdin.readline().split())

    tile_map = [[0 for j in range(side_size)] for i in range(side_size)]
    tile_map[side_size - y][x - 1] = -1

    solve(0, 0, side_size, side_size, side_size - y, x - 1)

    for line in tile_map:
        print(" ".join(map(str, line)))
