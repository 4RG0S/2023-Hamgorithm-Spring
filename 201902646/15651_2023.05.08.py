from sys import stdin
N, M = map(int, stdin.readline().split())
lst = []

def back():
    if len(lst) == M:
        print(" ".join(map(str, lst)))
        return
    for i in range(1, N+1):
        lst.append(i)
        back()
        lst.pop()
back()
