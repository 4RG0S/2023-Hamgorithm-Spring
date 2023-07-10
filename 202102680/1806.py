n, m = map(int,input().split())
nums = list(map(int,input().split()))

start, end = 0, 0  # 초기 포인터 위치
plus = 0 # 합 저장
length = 100001

while(True):
    if plus >= m:   # 부분 합이 m 이상일 경우
        length = min(length, end - start)   # 길이 비교해서 더 짧은 거 저장
        plus -= nums[start]     # start위치 바꾸니까 plus에서 nums 배열의 start 위치 빼줌
        start += 1  # start 위치 변경
    elif end == n:  # 범위 넘어감
        break
    else:
        plus += nums[end]   # end + 1 해주며 plus 에 더해줌
        end += 1

if length == 100001:    # 값이 변하지 않음
    print(0)
else:
    print(length)