import sys
input = sys.stdin.readline

paper = list()

def func(x, y, l):
    if l == 1:
        if paper[x][y]:
            return [0, 1]
        else:
            return [1, 0]
    else:
        hl = int(l/2)
        v = [a + b + c + d for a, b, c, d in
            zip(
                func(x, y, hl), func(x+hl, y, hl),
                func(x, y+hl, hl), func(x+hl, y+hl, hl)
            )]
        
        if not v[0]:
            return [0, 1]
        elif not v[1]:
            return [1, 0]
        else: 
            return v


def main():
    n = int(input())
    for _ in range(n):
        paper.append(list(map(int, input().split())))
    result = func(0, 0, n)
    for i in result:
        print(i)


if __name__ == '__main__':
    main()
