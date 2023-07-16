import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 포인터 및 변수 설정
left, right = 0, 0
sum = 0
count = 0

while left <= right:
    # 합과 m이 같을 경우, count를 증가시키고 
    # left 포인터가 가르키는 값을 빼고 포인터 이동
    if sum == m:
        sum -= arr[left]
        left += 1
        count += 1
    
    # 합이 m보다 작을 경우, 먼저 right 포인터의 위치를 확인
    # 포인터의 값이 n보다 크면 break
    # 이후 포인터가 가르키는 값을 더하고 포인터 이동
    elif sum < m:
        if right == n:
            break
        
        sum += arr[right]
        right += 1

    # 합이 m보다 클 경우, 포인터가 가르키는 값을 빼고 포인터 이동
    else:
        sum -= arr[left]
        left += 1

print(count)