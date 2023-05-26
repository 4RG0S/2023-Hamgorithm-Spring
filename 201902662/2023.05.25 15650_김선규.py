def main():
    n, m = list(map(int, input().split()))
    
    def prt(a, b, li):
        if a == 0:
            print(*li)
            return
            
        for i in range(b, n+1):
            prt(a-1, i+1, li+ [i])
            
    prt(m, 1, [])
    
if __name__ == "__main__":
    main()