n, m = map(int, input().split())
arr = [[] for i in range(n)] 	# 바닥 모양을 저장할 2차원 리스트

count = 0 # 총 판자의 개수

for i in range(n):
    arr[i] = (list(input()))
 
# 가로 판자의 개수
for i in range(n):
    a = ''
    for j in range(m):
        if arr[i][j] == '-':
            if arr[i][j] != a: 
                # 같은 모양일 때 하나로 치기 때문에 같은지 검사
                count += 1
        a = arr[i][j]
        # a에 해당 모양을 저장, 이어졌는지 확인
 
# 새로 판자의 개수
for j in range(m):
    a = ''
    for i in range(n):
        if arr[i][j] == '|':
            if arr[i][j] != a:
                count += 1
        a = arr[i][j]
 
print(count)