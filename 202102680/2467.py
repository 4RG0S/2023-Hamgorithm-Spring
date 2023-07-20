######## 이건 이분 탐색으로 푼 것 ########
n = int(input())
liquid = list(map(int, input().split()))
left, right = 0, 0
answer = 2000000000

for i in range(n-1):
    cur = liquid[i]

    start = i + 1
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        temp = cur + liquid[mid]    # 현재 값에 무언 갈 더하면서 이 값이 0에 가까워지게 만드는 값을 찾는 로직

        if abs(temp) < answer:
            answer = abs(temp)
            left = i
            right = mid
            if temp == 0:
                break
        if temp < 0:
            start = mid + 1     # 작으니까 더 큰 값을 더해보기 위해 start를 mid + 1 값으로 설정
        else:
            end = mid - 1       # 크니까 더 작은 값을 더해보기 위해 end를 mid - 1 값으로 설졍

print(liquid[left], liquid[right])

######## 이건 투 포인터로 푼 것 #########
n = int(input())
liquid = list(map(int, input().split()))
start, end = 0, n-1
answer = abs(liquid[start] + liquid[end])
left, right = start, end

while start < end:
    temp = liquid[start] + liquid[end]  # 양쪽 끝 값 합한 거

    if abs(temp) < answer:
        answer = abs(temp)
        left = start
        right = end

        if answer == 0:
            break

    if temp < 0:  # 작으니까 start에 +1
        start += 1
    else:         # 크니까 end에 -1
        end -= 1

print(liquid[left], liquid[right])

