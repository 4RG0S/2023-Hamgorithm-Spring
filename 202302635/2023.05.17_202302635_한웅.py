N = int(input())
paper = [[0]*100 for _ in range(100)]
c = 0
for i in range(N) :
    a , b = map(int,input().split())
    for j in range(89-a,99-a) :            
        for k in range(b,b+10) :
            paper[j][k] = 1
        
for i in range(100) :
    c += paper[i].count(1)

print(c)
        