import sys
input = sys.stdin.readline

n = int(input())

def sol(n, fr, tmp, to):
    if n<= 20:    
        if n==1:
            print(fr, to)
        else:
            sol(n-1, fr, to, tmp)
            print(fr, to)
            sol(n-1, tmp, fr, to)


print(2**n -1)
sol(n, 1, 2, 3)
