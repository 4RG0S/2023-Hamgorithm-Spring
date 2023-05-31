import copy

def main():
    n, m = list(map(int, input().split()))
    li = sorted(list(map(int, input().split())))
    
    def prt(a, numli, prtli):
        if a == m:
            print(*prtli)
            return
        
        inli = []    
        for i in range(0, len(numli)):
            e = numli[i]
            if e not in inli:
                newli = copy.deepcopy(numli)
                newli.remove(e)
                prt(a+1, newli, prtli+[e])
                inli.append(e)
    
    prt(0, li, [])
    
if __name__ == "__main__":
    main()