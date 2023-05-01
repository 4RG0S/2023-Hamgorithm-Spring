import sys
input = sys.stdin.readline

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    def func(i, j, n):
        v = [0, 0, 0]
        if n == 0:
            v[matrix[i][j]] += 1
        else:
            next_n = int(n/3)
            for a in range(3):
                for b in range(3):
                    result = func(i+a*n, j+b*n, next_n)
                    v[0] += result[0]
                    v[1] += result[1]
                    v[2] += result[2]
            if not v[1] and not v[2]:
                v = [1, 0, 0]
            elif not v[0] and not v[2]:
                v = [0, 1, 0]
            elif not v[0] and not v[1]:
                v = [0, 0, 1]
        return v
    result = func(0,0,int(n/3))
    print(result[-1])
    print(result[0])
    print(result[1])
    
if __name__ == '__main__':
    main()