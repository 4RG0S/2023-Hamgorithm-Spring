from sys import stdin
N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
begin, end = 0, 1
count = 0
while (begin <= end and end <= N):
    result = sum(arr[begin:end])
    if result < M:
        end += 1
    elif result > M:
        begin += 1
    else:
        count += 1
        end += 1
print(count)

