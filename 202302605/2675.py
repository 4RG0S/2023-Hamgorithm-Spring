t = int(input())

for i in range(t):
    r, s = map(str, input().split())
    R = int(r)
    for i in range(len(s)):
        print(s[i]*R, end='')
    print()