import sys

N = int(input())

X = list(map(int,sys.stdin.readline().split()))

copy_X = sorted(set(X)) # 이분 탐색을 위해 중복 값을 지우고 정렬

left,right = 0,len(copy_X)-1 # 탐색 지점 설정
mid = (left + right) // 2 # 중앙 기준 값 설정

for i in range(len(X)) :
    left,right = 0,len(copy_X)-1 # 탐색 후 다시 탐색 지점을 돌려놓음

    while(X[i] != copy_X[mid]) :
        mid = (left + right) // 2 # 중앙 값을 조정해나가며 목표 값 X[i]를 찾아나감

        if X[i] < copy_X[mid] :
            right = mid - 1
            
        elif X[i] > copy_X[mid] :
            left = mid + 1
    
    X[i] = mid

print(*X)