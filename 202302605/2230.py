import sys

n, m = map(int, sys.stdin.readline().split())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort() # 투 포인터 사용을 위해 정렬

start = 0
end = 0
dif = int(2e9) # 2e9 = 2*10^9 / 무한대를 표현

while end < n:
    if end < start:
        end += 1

    elif arr[end] - arr[start] >= m:
        dif = min(dif, arr[end] - arr[start])
        start += 1
        # 두 수의 차이가 dif보다 작으면 dif에 저장

    else:
        end += 1

print(dif)