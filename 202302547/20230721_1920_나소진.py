import sys


def search(arr, key, start, end):  # 이진탐색 재귀함수 정의
  if start > end:
    return None
  mid = (start + end) // 2  # mid를 인덱스 값으로 사용
  if arr[mid] == key:
    return 1
  elif arr[mid] > key:  # 중간 값이 key보다 크면 목록의 왼쪽 부분 확인
    return search(arr, key, start, mid - 1)
  else:  # 중간 값이 key보다 작으면 목록의 오른쪽 부분 확인
    return search(arr, key, mid + 1, end)


input = sys.stdin.readline
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
arr1.sort()  # 이진 탐색을 위해 탐색 대상인 arr1 정렬

for i in range(m):
  if search(arr1, arr2[i], 0, n - 1) == None:
    print(0)
  else:
    print(1)
