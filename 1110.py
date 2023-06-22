n = int(input())
on = n
cnt = 0

while True :
    if n < 10 :
        n1 = 0
        n2 = n
    else :
        n1 = (n // 10) 
        n2 = (n % 10) 
    n3 = n1 + n2 
    temp = n3 % 10 
    n = n2 * 10 + temp
    cnt += 1
    if n == on :
        print(cnt)
        break