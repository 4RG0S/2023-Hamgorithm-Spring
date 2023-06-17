n, a, b, t, r = map(int, input().split())

c = a

count1 = 0
count2 = 0

if a + t > b:
    print(-1)

else:
    while count1 < n:
        if a + t <= b:
            a += t
            count1 += 1

        else: 
            count2 += 1

            if a - r > c:
                a -= r
                
            else:
                a = c
                
    print(count1 + count2)