import sys
input = sys.stdin.readline

def main():
    dp = [0, 1, 1, 1, 2, 2]
    for i in range(5, 101):
        dp.append(dp[-1] + dp[-5])
    
    T = int(input())
    for i in range(T):
        n = int(input())
        print(dp[n])
    
if __name__ == '__main__':
    main()