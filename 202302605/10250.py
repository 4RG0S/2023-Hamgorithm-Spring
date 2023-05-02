t = int(input())

for i in range(t):
    h,w,n = map(int, input().split())

    ho = 0
    floor = 0

    a = int(n/h)   # ho
    b = n%h   # floor

    if a == 0 or n == h:
        ho = str(1)
    elif b == 0:
        ho = str(a)
    else:
        ho = str(a + 1)


    if b == 0:
        floor = str(h)
    else:
        floor = str(b)
    
    print(floor+ho)