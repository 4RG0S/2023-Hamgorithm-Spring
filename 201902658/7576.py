from collections import deque

column, row = map(int, input().split())  # 컬럼과 행의 크기 입력
graph = [list(map(int, input().split())) for _ in range(row)]  # 그래프 정보 입력
queue = deque([])  # BFS에 사용될 큐
delta_x, delta_y = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우 이동
max_day = 0  # 모든 토마토가 익는 데 필요한 최대 일수

# 그래프에서 익은 토마토 위치를 큐에 추가
for i in range(row):
    for j in range(column):
        if graph[i][j] == 1:
            queue.append([i, j])

# BFS 알고리즘 실행
def bfs():
    while queue:
        x, y = queue.popleft()  # 큐에서 토마토 위치 꺼내기
        for i in range(4):  # 상하좌우 체크
            next_x, next_y = delta_x[i] + x, delta_y[i] + y
            if 0 <= next_x < row and 0 <= next_y < column and graph[next_x][next_y] == 0:  # 안익은 토마토이면
                graph[next_x][next_y] = graph[x][y] + 1  # 하루 후 익게 함
                queue.append([next_x, next_y])  # 큐에 새로 익은 토마토 위치 추가

bfs()

for i in graph:
    for j in i:
        if j == 0:  # 안익은 토마토가 있으면 -1 출력 후 종료
            print(-1)
            exit(0)
    max_day = max(max_day, max(i))  # 가장 늦게 익는 토마토의 일수 확인

print(max_day - 1)  # 시작일이 1이었으므로 마지막에 1을 빼줌
