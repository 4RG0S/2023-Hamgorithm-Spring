#n_lst를 list로 만들면 시간초과
#set으로 만들면 탐색시간이 줄어들어서 시간초과 x
import sys
input = sys.stdin.readline
n = int(input())
n_lst = set(map(int, input().split()))
# n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))
# n_lst.sort()

for i in m_lst :
    if i in n_lst :
        print(1)
    else :
        print(0)
#이분탐색으로 해보니 for문으로 m_lst의 인덱스로 원소
#빼내서 비교하면 재귀함수 최대 호출범위를 넘어버림
#함수를 다시 짜야할듯
# def binarysearch(list, target, left, right) :
#     mid = (left + right) // 2
#     mid_val = list[mid]
#     if target == mid_val :
#         print(1)
#     elif mid_val > target :
#         binarysearch(list, target, left, mid - 1)
#     elif mid_val < target :
#         binarysearch(list, target, mid + 1, right)
#     else :
#         print(0)

# for i in range(m) :
#     binarysearch(n_lst, m_lst[i], 0, n - 1)

