import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    li.sort(key=lambda x : [x[1], x[0]])
    v = li[0][1]
    max = 1
    for i in range(1,n):
        if v <= li[i][0]:
            v = li[i][1]
            max += 1
    print(max)
    
if __name__ == '__main__':
    main()