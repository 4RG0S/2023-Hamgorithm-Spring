from collections import deque

test_cases = int(input())
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 상, 하, 우, 좌 방향을 나타내는 배열


def breadth_first_search(row, col):
    queue = deque()
    queue.append((row, col))

    while queue:
        row, col = queue.popleft()

        grid[row][col] = 0  # 해당 노드를 방문했음을 표시

        for i in range(4):
            next_row, next_col = row + directions[i][0], col + directions[i][1]

            # 새로운 위치가 격자 내에 있는지, 그리고 아직 방문하지 않은 노드인지 확인
            if (0 <= next_row < rows) and (0 <= next_col < cols) and (grid[next_row][next_col] == 1):
                grid[next_row][next_col] = 0  # 방문한 노드로 표시
                queue.append((next_row, next_col))

    return True


for i in range(test_cases):
    result = 0  # 연결된 구성 요소 수를 저장할 변수

    cols, rows, nodes = map(int, input().split())
    grid = [[0] * cols for _ in range(rows)]  # 격자를 초기화

    for j in range(nodes):
        x, y = map(int, input().split())
        grid[y][x] = 1  # 격자에 노드를 추가

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # 노드가 아직 방문되지 않았는지 확인
                breadth_first_search(row, col)
                result += 1  # 연결된 구성 요소의 수 증가

    print(result)  # 연결된 구성 요소의 수 출력
