import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
h = {}

def solve(s, e):
    if s >= e:
        return True
    else:
        if (s, e) in h:
            return h[(s, e)]
        else:
            if arr[s] != arr[e]:
                h[(s, e)] = False
                return False
            else:
                h[(s, e)] = solve(s + 1, e - 1)
                return h[(s, e)]

result = ""

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    s = s - 1
    e = e - 1
    if solve(s, e):
        result += "1\n"
    else:
        result += "0\n"

print(result)
