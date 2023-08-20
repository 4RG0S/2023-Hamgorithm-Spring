import sys

input = sys.stdin.readline
a, b = map(int, input().split())
dict1 = {}
for i in range(b):
    k = input().strip()
    dict1[k] = i

# 오름차순으로 정렬
result = sorted(dict1.items(), key=lambda x: x[1])

# 제한수가 신청수보다 더 많을 때 인원 넘어가면 break
for i in range(a):
    if i < len(result):
        print(result[i][0])
    else:
        break
