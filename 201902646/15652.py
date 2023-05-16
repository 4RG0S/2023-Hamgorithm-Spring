from sys import stdin
N, M = map(int, stdin.readline().split())
lst = []

def back(start):
    if len(lst) == M:
        print(" ".join(map(str, lst)))
        return
    for i in range(start, N+1):
        lst.append(i)
        back(i)
        lst.pop()
back(1)
