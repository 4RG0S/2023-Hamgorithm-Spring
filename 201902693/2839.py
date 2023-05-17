import sys
input = sys.stdin.readline
n = int(input())

# n이 5로 나눠떨어지면 그 몫이 최소
# 이외에는 n을 3씩 줄여보면서 3의 배수, 5의 배수의 조합으로
# n을 만들 수 있는지 확인해본다.
# 3씩 줄이다가 5로 나누어 떨어지면 5로 나눈 몫과 3을 줄인 만큼이 최소주머니 개수
# 3씩 줄이다가 0이 되면 3으로만 만들 수 있는 3의 배수이므로 3으로 나눈 몫이 최소주머니 개수
# 3씩 줄이다가 1, 2가 남으면 만들 수 없는 수이므로 -1을 출력 
if n % 5 == 0 :
    print(n //5)
else :
    cnt = 0
    while n > 0 :
        n -= 3
        cnt += 1
        if n % 5 == 0 :
            cnt += n//5
            print(cnt)
            break
        elif n == 0 :
            print(n // 3)
            break
        elif n == 1 or n == 2 :
            print(-1)
            break