A,B = map(int, input().split())

a = A

result = 0

b = 0

key = 0

while a >= B :
    temp_a = a
    temp_B = B

    if a/2 != int(a/2) :
        while (True) :
            if a/2 != int(a/2) :
               a -= 1
               B -= 1
            else :
               a /= 2
            
            if B < 0 :
                a = temp_a
                B = temp_B
                break

            if a <= B :
                key = 1
                break      
            
        if key == 1 :
            break 

        result += 2**b
        a += 1

    else :
        a /= 2
        b += 1

print(result)
