n, c = map(int,input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()


start, end = 1, arr[-1]-arr[0]  # 앞 집부터 공유기 설치
answer = 0

while start <= end:
    mid = (start + end) // 2    # 첫 점과 끝 점의 중간을 Mid 초기 값으로 설정
    cur = arr[0]                # 현재 가리키는 부분은 배열의 첫번째 값
    count = 1

    for i in range(1, len(arr)):
        if arr[i] >= cur + mid:     # 배열의 값이 현재 가리키는 곳에서 mid를 더한 것보다 크거나 같을 때 설치.
            count += 1          # 공유기 지금까지 몇 개 설치했나 count
            cur = arr[i]      # 그 다음을 비교하기 위해 가리키는 값을 바꿔줌

    if count >= c:
        start = mid + 1     # 공유기 갯수보다 설치한 게 더 많으니까 간격을 더 넓혀서 mid+1 을 start 로 설정
        answer = mid
    else:
        end = mid - 1       # 공유기 갯수보다 더 적게 설치했으므로 간격을 더 좁혀서 mid-1 을 end 로 설정

print(answer)