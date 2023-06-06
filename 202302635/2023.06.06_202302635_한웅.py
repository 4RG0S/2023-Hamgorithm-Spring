ls = []
r = 0
while True :
    a = list(map(int,input().split()))
    r = sum(a)
    
    
    if r == 0 :
        break
    if r <= max(a)*2 :
        print("Invalid")
    elif a[0] == a[1] or a[1] == a[2] or a[0] == a[2] :
        if a[0] == a[1] == a[2] :
            print("Equilateral")
        else :print("Isosceles")
    else :
        print("Scalene")
