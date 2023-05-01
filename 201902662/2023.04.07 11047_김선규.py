import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    li = [int(input()) for _ in range(n)]
    num = 0
    for i in range(n-1, -1, -1):
        if li[i] <= k:
            num += k//li[i]
            k -= li[i]*(k//li[i])
    print(num)
    
if __name__ == '__main__':
    main()