# n = int(input())
# count = 0
# num = list(map(int, input().split()))

# for i in range(n):
#     if num [i] != 1 and num[i]%2 != 0 and num[i]%3 != 0 and num[i]%5 != 0 and num[i]%7 != 0 and num[i]%11 != 0 and num[i]%13 != 0 and num[i]%17 != 0 and num[i]%19 != 0 and num[i]%23 != 0 and num[i]%29 != 0 and num[i]%31 != 0:
#         count += 1
#     elif num[i] == 2 or num[i] == 3 or num[i] == 5 or num[i] == 7 or num[i] == 11 or num[i] == 13 or num[i] == 17 or num[i] == 19 or num[i] == 23 or num[i] == 29 or num[i] == 31:
#         count += 1

# print(count)

# 위는 1000보다 작은 소수를 모두 걸러낸 개 쓰레기 같은 내 코드
    
n = int(input())
numbers = map(int, input().split())
sosu = 0

for num in numbers:
    error = 0
    if num > 1 :
        for i in range(2, num):
            if num % i == 0:
                error += 1
        if error == 0:
            sosu += 1

print(sosu)