import sys
input = sys.stdin.readline
N = int(input())

row = [0 for _ in range(N)]
result = 0
# x는 row, row[x] = col, row[x] = 현재 Queen의 위치
def is_promising(x):
    for i in range(x):
        # abs(x - i) = abs(row[x] - row[i]) 행과 열의 차가 같으면 안됨 => 대각선에 있음
        # row[x] = rox[i] 같은 열에 있는 경우 불가능
        # x == 내가 현재 놓은 퀸의 row, i = 위에있는 퀸의 row
        if (row[x] == row[i]) or (abs(row[x] - row[i]) == abs(x - i)):
            return False
    return True

def dfs(x):
    global result
    # 끝까지 다 처리된 경우
    if x == N:
        result += 1
    else:
        # 각 행에 퀸을 놓는다.
        for i in range(N):
            # 왜 넣어줄까? [x][i] 에 넣고 가능한지 돌리기 위해서
            row[x] = i
            if is_promising(x):
                dfs(x+1)

dfs(0)
print(result)