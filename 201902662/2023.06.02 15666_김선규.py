def main():
    n, m = list(map(int, input().split()))
    li = sorted(list(map(int, input().split())))
    
    def prt(level, prev, prtli):
        if level == m:
            print(*prtli)
            return
        
        inli = []    
        for i in range(0, n):
            e = li[i]
            if  e >= prev and e not in inli:
                prt(level+1, e, prtli+[e])
                inli.append(e)
    
    prt(0, 0, [])
    
if __name__ == "__main__":
    main()