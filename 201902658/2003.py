N, M = map(int, input().split())
sequence = list(map(int, input().split()))

result = 0

current_sum = sequence[0]
start = 0
end = 1

# '투 포인터' 알고리즘 시작
while end <= N and start <= end:
    if current_sum == M:
        result += 1
        current_sum -= sequence[start]
        start += 1

    elif current_sum < M:
        if end == N:
            break
        current_sum += sequence[end]
        end += 1
    else:
        current_sum -= sequence[start]
        start += 1

print(result)