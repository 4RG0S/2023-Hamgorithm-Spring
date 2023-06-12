N , M = map(int,input().split())
A = list(map(int,input().split()))
m_s = 0


for i in range(N-2) : 
    for j in range(1+i,N-1) :
        for k in range(1+j,N) :
            s = A[i] + A[j] + A[k]
            if s <= M and s > m_s :
                m_s = s 
print(m_s)