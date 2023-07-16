import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr =  list(map(int,input().split())) 
arr.sort()

start, end = 0, 0
sum = 0
len = sys.maxsize

while True : 
    if sum >= s : # 합이 s보다 크면 오른쪽으로 옮겨보면서 길이 확인
        len = min(len, end - start)
        sum -= arr[start]
        start += 1
    elif end == n : 
        break
    else : # 합이 s보다 작으면 왼쪽으로 옮겨보면서 길이 확인
        sum += arr[end]
        end += 1

if len == sys.maxsize : # 합을 만드는 것이 불가능한 case
    print(0)
else : 
    print(len)
    
# 미해결 문제...