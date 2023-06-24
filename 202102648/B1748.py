import sys
input = sys.stdin.readline

n = int(input())
ans = 0


for i in range(len(str(n))-1):
    ans += 9 * (10 ** i) * (i + 1)

ans += ((int(n) - (10 ** (len(str(n))-1))) + 1) * ((len(str(n))-1) + 1)

print(ans)