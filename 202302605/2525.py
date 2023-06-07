a, b = map(int, input().split())

c = int(input())

if b + c >= 60:
    h = (b + c) // 60
    m = (b+c)%60

    if a + h >= 24:
        h = (a+h)%24
    
    else:
        h = a+h

else:
    m = b+c
    h = a

print(h,m)