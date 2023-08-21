import sys
n = int(sys.stdin.readline())
d = {}
for i in range(n) :
    a , b = input().split()
    if b == 'enter' : #출근시 리스트에 추가
        d[a] = b
    elif b == 'leave' : #퇴근시 리스트에서 제거
        del d[a]

ds = sorted(d , reverse = True)

print(*ds , sep='\n')