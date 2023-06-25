import sys


def divide_conquer(x, y, N):
    global cut, blue
    color = paper[x][y]

    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                divide_conquer(x, y, N // 2)
                divide_conquer(x, y + N // 2, N // 2)
                divide_conquer(x + N // 2, y, N // 2)
                divide_conquer(x + N // 2, y + N // 2, N // 2)
                return 0
    if color == 0:
        cut += 1
    else:
        blue += 1


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    paper = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

    cut, blue = 0, 0
    divide_conquer(cut, blue, N)
    print(cut)
    print(blue)
