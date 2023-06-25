def main():
    n, m = list(map(int, input().split()))
    num = sorted(list(map(int, input().split())))
    
    def prt(li):
        if len(li) == m:
            print(*li)
            
        for i in num:
            if i > li[-1]:
                prt(li + [i])
    
    for i in num:
        prt([i])
    
if __name__ == "__main__":
    main()