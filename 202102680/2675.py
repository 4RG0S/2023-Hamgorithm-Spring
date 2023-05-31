import sys
T = int(input())

for i in range(T):
    r, s = sys.stdin.readline().split()

    for c in s:
        print(c * int(r), end = "")
    print()