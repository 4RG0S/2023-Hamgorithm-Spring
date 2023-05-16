import sys, math
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    lst = list(map(int, input().split()))
    n = lst[0]
    lst = lst[1:]
    ans = 0

    for i in range(n):
        for j in range(i+1, n):
            ans += math.gcd(lst[i], lst[j])
    print(ans)


