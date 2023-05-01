import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = [int(input()) for _ in range(n)]
    dp = [0 for _ in range(n)]
        
    if n > 2:
        dp[0] = li[0]
        dp[1] = dp[0]+li[1]
        for i in range(2,n):
            dp[i] = max(dp[i-3]+li[i-1]+li[i], dp[i-2]+li[i])
        print(dp[-1])
    else:
        print(sum(li))
    
if __name__ == '__main__':
    main()