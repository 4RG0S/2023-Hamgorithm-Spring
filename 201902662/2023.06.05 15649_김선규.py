import copy

def main():
    m, n = list(map(int, input().split()))
    
    def prt(ck, li):
        if len(li) == n:
            print(*li)        
        
        for i in range(1, m+1):
            if i not in ck:
                prt(ck+[i], li+[i])
    prt([], [])
    
if __name__ == '__main__':
    main()