n, m = map(int,input().split())
nums = list(map(int,input().split()))

end = 0
count = 0   # 합을 나타낼 수 있는 개수 => 답
plus = 0    # 합을 나타내는 변수

for start in range(n):  # 시작점을 다르게 해서 모든 경우의 수 검사 ( 현재 부분 합이 m 보다 큰 경우 반복문 재시작 -> start + 1)
    plus = nums[start]
    end = start     # 시작점과 끝점 동일하게 둠
    while(plus <= m):   # 현재 부분 합이 같거나 작을 경우에만 반복문 돌게 함
        if plus == m:   # 현재 부분 합이 m 과 같다면 count + 1
            count += 1
            break
        else:
            end += 1    # 현재 부분 합이 m 보다 작은 경우 end + 1
            if end >= n:
                break
            plus += nums[end]


print(count)

