n = int(input())
decimal = [True for _ in range(n+1)]
decimal[0] = decimal[1] = False

for i in range(2, int(n**0.5) + 1):
    if decimal[i]:
        for j in range(i*i, n+1, i):
            decimal[j] = False
        
# 소수들의 배열만 새롭게 정의하여 기존 n ^ 2의 복잡도에서 n의 복잡도로 줄일 수 있다.
decimals = [i for i in range(n+1) if decimal[i]]

count = 0
for i in range(len(decimals)):
    sum = 0
    for j in range(i, len(decimals)):
        sum += decimals[j]
        if sum > n:
            break
        elif sum == n:
            count += 1
            break
print(count)

# 투 포인터를 사용하여 최적화 할 수 있었지만 여백이 부족한 관계로 생략하였다.