n, m = map(int,input().split())
nums = list(map(int,input().split()))

plus = []   # 더한 값 저장하는 리스트
big = 0
plus.append(sum(nums[:m]))

for i in range(n - m):
    plus.append(plus[i] - nums[i] + nums[m + i])    # 더하는 범위 옮겨주기

print(max(plus))    # 리스트에서 가장 큰 값 출력