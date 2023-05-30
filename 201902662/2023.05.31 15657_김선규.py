def main():
    n, m = list(map(int, input().split()))
    num = sorted(list(map(int, input().split())))
    
    def prt(a, b, li):
        if a == m:
            print(*li)
            return
            
        for i in range(b, n):
            prt(a+1, i, li+[num[i]])
    
    prt(0, 0, [])
    
if __name__ == "__main__":
    main()