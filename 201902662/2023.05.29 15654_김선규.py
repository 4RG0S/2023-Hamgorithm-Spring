def main():
    n, m = list(map(int, input().split()))
    num = sorted(list(map(int, input().split())))
    
    def prt(a, li):
        if a > m:
            print(*li)
            return
            
        for i in range(0, n):
            if num[i] not in li:
                prt(a+1, li+[num[i]])
    
    prt(1, [])
    
if __name__ == "__main__":
    main()