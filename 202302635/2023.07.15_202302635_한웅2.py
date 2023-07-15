import math

N = int(input())

#에라토스테네스의 체 이용
a = [False, False] + [True] * (N-1)
pn = []

for i in range(2, N+1):
    if a[i]:
        pn.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False

result = 0
start = 0
end = 0

#투포인터
while end <= len(pn):
    s = sum(pn[start:end])
    if s == N:
        result += 1
        end += 1
    elif s < N:
        end += 1
    else:
        start += 1

print(result)