def main():
    n, k = map(int, input().split())
    buy_bottle = 0
    cnt = bin(n).count('1')
    while(cnt > k):
        buy_bottle += 1
        n += 1
        cnt = bin(n).count('1')
    print(buy_bottle)      
        
if __name__ == '__main__':
    main()
