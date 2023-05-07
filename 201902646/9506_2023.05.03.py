def suma(N):
    temp = 0;
    t = 0;
    temp2 = []
    temp3 = 0;
    for i in range(1, N):
        if N % i == 0:
            temp += i
            temp2.append(i)
    if temp == N:
        print(N, "=", end=" ")
        for j in range(len(temp2)):
            print(temp2[j], end = " ")
            if j < len(temp2) - 1:
                print("+", end = " ")
        print("")
    elif N > 0 and temp != N:
        print(N, "is NOT perfect.")
while True:
    n = int(input())
    suma(n)
    if n == -1:
        break;
