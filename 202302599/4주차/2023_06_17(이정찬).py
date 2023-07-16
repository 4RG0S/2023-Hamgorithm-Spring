A = int(input())

answer = A

B = [64]

i = 0

result = 0

while answer != 0 :
    if A == 64 :
        result += 1
        break

    B.append(B[len(B)-1])
    B[len(B)-1] /= 2
    B[len(B)-2] /= 2

    if B[len(B)-1] > answer :
        B.pop()
    
    else : 
        answer -= B[0]
        del B[0]
        result += 1
        
print(result)