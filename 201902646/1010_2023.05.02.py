from sys import stdin
T = int(stdin.readline())

def fact(x):
    n = 1
    for i in range(1, x+1):
        n *= i
    return n
        
for i in range(T):
    M, N = map(int, stdin.readline().split())
    bridge = fact(N) // (fact(M)*fact(N-M))
    print(bridge)
