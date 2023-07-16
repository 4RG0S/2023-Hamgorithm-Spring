import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
sum = 0
leng = int(2e9)

while start <= end:
    if sum >= s: 
        leng = min(leng, end - start)
        sum -= arr[start]
        start += 1

        # 합이 s보다 크다면 (send - start)와 저장된 길이와 비교
        # 그리고 arr[start] 빼기
        # start 포인터 오른쪽 한 칸 이동
    
    elif end == n:
        break
    
    else:
        sum += arr[end]
        end += 1

        # 합이 s보다 작다면 현재 end 포인터 값을 더하기
        # end 포인터 오른쪽으로 한 칸 이동

if leng == int(2e9):
    print(0)

else:
    print(leng)