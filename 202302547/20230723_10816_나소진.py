import sys
from collections import Counter  # 리스트 중복 값 반환 모듈

input = sys.stdin.readline
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
arr1.sort()  # 이진 탐색을 위해 탐색 대상인 arr1 정렬

count = Counter(arr1)  # arr1에 있는 중복 값 확인

for i in range(m):
  if arr2[i] in count:  # arr1에 있는 중복 값(count 딕셔너리)과 같으면 횟수 출력
    print(count[arr2[i]], end=' ')
  else:
    print(0, end=' ')
""" 
for i in range(m) :
  count,start = 0,0
  end = n-1 
  while start <= end :
   mid = (start + end) // 2 
   if arr1[mid] == arr2[i] : 
     count += 1
     if mid+1 < end and arr1[mid+1] == arr2[i] :
       start = mid + 1
     elif mid-1 > start and arr1[mid-1] == arr2[i] :
       end = mid - 1
     else :
       continue
   elif arr1[mid] > arr2[i] :
     end = mid - 1
   else :
     start = mid + 1 
  print(count)

이 방법으로 구현하려고 했으나 KeyboardInterrupt 예외처리 실패..
"""
