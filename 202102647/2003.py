import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
count = 0
start = 0
end = 0
total = 0
while start <= end and end <= N:
    total = sum (A[start:end])
    if total > M:
        start += 1

    elif(total < M):
        end += 1
    else:
        end += 1
        count += 1
print(count)
