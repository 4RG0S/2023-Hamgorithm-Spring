T = int(input())
Q , D , N , P = 0 , 0 , 0 , 0
for i in range(T) :
    C = int(input())
    Q = C // 25
    D = (C - (25 * Q)) // 10
    N = (C - (25 * Q) - (10 * D)) // 5
    P = (C - (25 * Q) - (10 * D) - (5 * N)) // 1
    print(Q, D, N, P)

