# 이진탐색 시작
def binarysearch(arr,target):
    left = 0
    right = len(arr)-1
    result = -1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] < target: 
            #mid의 값이 target보다 작다면 그 앞에 있는 값들도 target보다 작다는 것 
            # -> count에 모두 담은 후 left를 mid의 오른쪽 index로 지정
            result = mid
            left = mid +1
        else:
            # mid 자리의 값이 target보다 크면 그 왼쪽을 탐색
            right = mid -1
    return result

import sys
testcase = int(sys.stdin.readline().rstrip())
# testcase 개수에 따라 입력 받은 후 탐색
for _ in range(testcase):
    fish = list(map(int,sys.stdin.readline().split()))
    A = sorted(list(map(int,sys.stdin.readline().split())))
    B = sorted(list(map(int,sys.stdin.readline().split())))
    
    count = 0
    for i in (A):
        count += binarysearch(B,i)+1
    print(count)
