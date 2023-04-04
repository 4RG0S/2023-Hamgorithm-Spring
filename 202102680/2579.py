n = int(input())

l = []

for _ in range(n):
    l.append(int(input()))

dp=[0]*(n) # dp 리스트
if len(l)<=2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(l))
else: # 계단이 3개 이상일 때
    dp[0]=l[0] # 첫째 계단 수동 계산
    dp[1]=l[0]+l[1] # 둘째 계단까지 수동 계산
    for i in range(2,n): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
        dp[i]=max(dp[i-3]+l[i-1]+l[i], dp[i-2]+l[i])
    print(dp[-1])