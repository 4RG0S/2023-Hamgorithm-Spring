import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = []
    for i in range(n):
        li.append(list(map(int, input().split())))
        for j in range(n):
            if li[i][j] == 0:
                li[i][j] = 10000
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                li[j][k] = min(li[j][k], li[j][i] + li[i][k])
    
    for i in range(n):
        for j in range(n):
            if li[i][j] == 10000:
                li[i][j] = 0
            else:
                li[i][j] = 1
    
    for i in li:
        print(*i)
    
if __name__ == '__main__':
    main()