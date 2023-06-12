A,B = map(int,input().split())

C = [True] * (B-A+1)


for i in range(2,B) :
    if int(A/i) == A/i :    
        for j in range(A,B+1,i) :
            if i == j :
                continue
            if j >= A and j <= B :
                C[j-A] = False
    else : 
        for j in range(((int(A/i))+1)*(i),B+1,i) :
            if i == j :
                continue
            if j >= A and j <= B :
                C[j-A] = False


for i in range(len(C)) :
    if i+A == 1 :
        continue
    if C[i] :  
        print(i+A)
