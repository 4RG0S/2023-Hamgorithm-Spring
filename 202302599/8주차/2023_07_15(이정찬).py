import sys

N,d,k,c = map(int, input().split())

con_sushi = []

start = 0
end = k

checking = set() # 중복 되는 회전 초밥 떄문에 리스트 대신 집합 사용

count = 0
temp_count = 0

for _ in range(N) :
    con_sushi.append(int(sys.stdin.readline()))

for i in range(k) : # 리스트 끝에서 리스트 k번째까지가 정답이 될 수도 있기에 리스트애 추가적으로 앞쪽 수들을 넣어줌
    con_sushi.append(con_sushi[i])

while start <= N :
    checking = set()
    for i in range(start,end) :
        checking.add(con_sushi[i])

    checking.add(c) # 쿠폰 초밥이 없을 경우를 계산
    temp_count = len(checking) 

    if temp_count > count :
        count = temp_count
    
    start += 1
    end += 1

print(count)