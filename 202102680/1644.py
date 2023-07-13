N = int(input())

# 소수 구하기 (에라토스테네스의 체)
a = [False, False] + [True] * (N-1)
prime = []

for i in range(2, N+1):
    if a[i]:
        prime.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False

# 투 포인터 활용
answer = 0
start = 0
end = 0
if N == 1:
    temp_sum = 0
else:
    temp_sum = prime[0]
while start < len(prime) and end < len(prime):
    if temp_sum == N:   # 같으면 answer+1
        answer += 1
        end += 1    # 끝 증가
        if end == len(prime):   # 범위 벗어나면 break
            break
        temp_sum = temp_sum + prime[end]
    elif temp_sum < N:      # 작으면 end + 1
        end += 1
        if end == len(prime):   # 범위 벗어나면 break
            break
        temp_sum = temp_sum + prime[end]
    else:   # 커졌을 경우
        temp_sum = temp_sum - prime[start]
        start += 1  # 앞쪽 포인터 start +1


print(answer)