import sys
input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n) :
    a, b = input().split()
    a = int(a)
    lst.append([a, b])
lst.sort(key = lambda x : x[0])

for i in lst :
    print(*i)

# lambda를 이용하여 정렬하는 문제
# key = lambda를 이용하여 정렬할 기준을 정할 수 있다.