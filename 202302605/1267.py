n = int(input())
t = list(map(int, input().split()))

Y = 0
M = 0

for i in range(n):
    Y += 10 * int(t[i]/30 + 1)
    M += 15 * int(t[i]/60 + 1)

if Y < M:
    print('Y', Y)
elif Y == M:
    print('Y M', Y)
else:
    print('M', M)