import sys
def solution(x, y, N):
    global minus_one, zero, one
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                for k in range(3):
                    for p in range(3):
                        solution(x + k * N // 3, y + p * N // 3, N // 3)
                return
    #print(color)
    if color == 0:
        zero += 1
    elif color == 1:
        one += 1
    elif color == -1:
        minus_one += 1

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    minus_one, zero, one = 0, 0, 0
    solution(0, 0, N)
    print(f'{minus_one}\n{zero}\n{one}')
