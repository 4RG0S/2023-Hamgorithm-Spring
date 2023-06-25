import sys
input = sys.stdin.readline
n = int(input())
input_lst = []
for i in range(n) :
    a, b = map(int, input().split())
    input_lst.append([a, b])
#lambda 이용해서 sort의 우선순위 부여
input_lst.sort(key = lambda x : (x[1], x[0]))

for i in input_lst :
    print(*i)