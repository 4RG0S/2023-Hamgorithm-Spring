import sys

N, S = map(int, input().split())
num = list(map(int, input().split()))

left, right = 0, 0 # 투포인터 시작
s = 0 
r = 100000000

while True:
    
    if s >= S:
        r = min(r, right - left)
        s -= num[left]
        left += 1
    elif right == N:
        break
   
    else:
        s += num[right]
        right += 1

if r == 100000000:   #불가능할 경우 0 출력
    print(0)
else:
    print(r)