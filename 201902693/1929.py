import sys
import math
input = sys.stdin.readline

def primeNumber(n) :
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0:
            return False
    return True

start, end = map(int, input().split())

for i in range(start, end + 1) :
    if primeNumber(i) :
        print(i)
        
#구글 답안
#함수를 사용안하니 시간이 더 오래걸렸다.
#함수 사용시 3100ms, 사용안하면 5572ms
# m,n=map(int,input().split())

# for i in range(m,n+1):
#     if i==1:#1은 소수가 아니므로 제외
#         continue
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0: #약수가 존재하므로 소수가 아님
#             break   #더이상 검사할 필요가 없으므로 멈춤
#     else:
#         print(i)