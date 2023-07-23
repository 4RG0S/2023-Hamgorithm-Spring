import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
start, end, sum = 0, 0, 0
result = []

for i in range(n): #i = start
    while sum < s and end < n: #부분합이 s이상이 되거나, end가 수열의 끝까지 탐색하면 종료
        sum += arr[end]
        end += 1

    if sum >= s: #부분합이 s이상이 된 경우에만 result에 결과값을 추가.
        result.append(end - i) #12번째 줄에서 end+=1 해서 반복문을 나왔기 때문에 end - i + 1 "- 1"

    sum -= arr[i]

result.sort()

if len(result) == 0:
    print(0)
else:
    print(result[0])