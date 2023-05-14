import sys
input = sys.stdin.readline
# readline안쓰면 시간이 10배이상 걸림... 앞으론 readline을 쓰도록하자
n = int(input())
result = []
for _ in range(n) :
    a, b = map(int, input().split())
    result.append([a, b])
result.sort()  

for i in range(len(result)) :
    print(*result[i])