import sys
input = sys.stdin.readline

N = int(input())

stack = []
result = []
now = 1
isTrue = True
for _ in range(N):
    num = int(input())
    while now <= num:
        stack.append(now)
        result.append('+')
        now += 1
    tmp = stack.pop()
    if tmp == num:
        result.append('-')
    else:
        print("NO")
        isTrue = False
        break

if isTrue:
    for txt in result:
        print(txt)