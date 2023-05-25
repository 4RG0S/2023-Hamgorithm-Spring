import sys
sys.setrecursionlimit(15000)

N, M = map(int, input().split(' '))

arr = []

def backtracking():
    for i in range(1, N + 1):
        if len(arr) == M:
            print(' '.join(map(str, arr)))
            return
        arr.append(i)
        backtracking()
        arr.pop()

backtracking()