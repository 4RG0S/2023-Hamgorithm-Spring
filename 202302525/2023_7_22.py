k, n = map(int, input().split())
lan = []
result_table = []

for _ in range(k):
    lan.append(int(input()))

lan.sort()

start = 1 #만들 수 있는 최소길이
end = lan[-1] #만들 수 있는 최대길이


while start <= end: #최소길이~최대길이 사이 이분탐색 진행
    cnt = 0
    mid = (start + end) // 2

    for i in lan:
        result = i // mid
        cnt += result

    if cnt < n:
        end = mid - 1

    elif cnt >= n:
        start = mid + 1
        result_table.append(mid)

result_table.sort()
print(result_table[-1])