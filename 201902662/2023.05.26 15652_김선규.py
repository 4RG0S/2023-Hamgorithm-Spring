def main():
    n, m = list(map(int, input().split()))
    
    def prt(a, b, li):
        if a > m:
            print(*li)
            return
            
        for i in range(b, n+1):
            prt(a+1, i, li+[i])
            
    prt(1, 1, [])
    
if __name__ == "__main__":
    main()