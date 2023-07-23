N = int(input())
A = list(map(int, input().split()))
M = int(input())
a = list(map(int, input().split()))
A.sort()			# A 정렬


for i in a:
    f, l = 0, N - 1		# 맨앞과 맨뒤
    X = False		# 정수가 존재하는지 여부 

    # 이분탐색 시작
    while f <= l:		
        mid = (f + l) // 2	
        if i == A[mid]:	
            X = True	
            print(1)		
            break		
        elif i > A[mid]:	
            f = mid + 1	
        else:			# A
            l = mid - 1	

    if not X:		# 찾지 못한 경우 0 출력
        print(0)		