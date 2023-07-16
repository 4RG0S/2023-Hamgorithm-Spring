a = int(input())
A = []

for t in range(a) :
    B = list(map(int, input().split()))
    obj = B[1] - B[0]
    
    begin = 1
    end = 1
    ans = 2
    res = begin + end

    if obj == 2 :
        print("2")
    elif obj == 1 :
        print("1")
    else :
        while res < obj :
            begin += 1 
            end += 1

            res += begin + end

            ans += 2
    
        if res > obj :
            if res-begin+1 > obj :
                ans -= 1

        print(ans) 

            


