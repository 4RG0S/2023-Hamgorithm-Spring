n = int(input())
a = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

a.sort()    # a의 원소 크기대로 정렬

# arr의 각 원소별로 이분탐색
for num in arr:
    f = 0           # 맨 처음(first)
    l = n - 1	    # 맨 뒤(last)
    Exist = False	# 존재 여부

    # 이분탐색 시작
    while f <= l:		    # first가 last보다 커지면 while문 탈출
        mid = (f + l) // 2	# mid는 first와 last의 중간값
        
        if num == a[mid]:	# num과 a[mid]가 같다 => 목표값 존재
            Exist = True	# Exist Ture 변경
            print(1)		
            break		    # 다음 원소 비교
        
        elif num > a[mid]:	# a[mid]가 num보다 작으면
            f = mid + 1	    # fisrt를 높임
        
        else:			    # a[mid]가 num보다 크다면
            l = mid - 1	    # last를 낮춤

    if Exist == False:		# 찾지 못한 경우
        print(0)

# 에라 시발 드럽게 어렵네 그지같은거