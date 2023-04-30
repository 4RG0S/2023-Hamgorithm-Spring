t = int(input())

for _ in range(t):
    ho = list(range(1, 15))
    k = int(input())
    n = int(input())
    sum = 0

    for _ in range(k):
        down_ho = [0] * 14
        for i in range(n): #n=3->i=0,1,2
            for j in range(i+1):
                down_ho[i] += ho[j]

        ho = down_ho
    

    print(down_ho[n-1])