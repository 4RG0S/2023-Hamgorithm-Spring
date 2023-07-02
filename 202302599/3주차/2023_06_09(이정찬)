A,B = map(int,input().split())

C = [True] * (B-A+1)


for i in range(2,int(B**(1/2))+1) :
    if int(A/i**2) == A/(i**2) :
        for j in range(A,B+1,i**2) :
            if j >= A and j <= B :
                C[j-A] = False
    else :
        for j in range(((int(A/i**2))+1)*(i**2),B+1,i**2) :
            if j >= A and j <= B :
                C[j-A] = False
        
            
result = 0

for i in range(len(C)) :
    if C[i] :
        result += 1

print(result)
