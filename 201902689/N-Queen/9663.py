import sys
input = sys.stdin.readline
N = int(input())

row = [0 for _ in range(N)]
result = 0
# x는 col
def is_promising(col):
    for i in range(x):
        # abs(x - i) = abs(row[x] - row[i]) 행과 열의 차가 같으면 안됨
        # row[x] = rox[i] 같은 행에 있는 경우라 안됨
        if (row[x] == row[i]) or (abs(row[x] - row[i]) == abs(x - i)):
            return False
    return True

def dfs(x):
    global result
    # 끝까지 다 처리된 경우
    if x == N:
        result += 1
    else:
        # 행 전체를 다 돌아야함
        for i in range(N):
            # 
            row[x] = i
            if is_promising(x):
                dfs(x+1)

dfs(0)
print(result)