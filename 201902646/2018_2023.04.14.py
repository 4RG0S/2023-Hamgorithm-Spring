from sys import stdin
N = int(stdin.readline())
begin, end = 0, 0
count, result = 0, 0
while (begin <= end and end <= N):
    if result < N:
        end += 1
        result += end
    elif result > N:
        begin += 1
        result -= begin
    else:
        count += 1
        end += 1
        result += end
print(count)
