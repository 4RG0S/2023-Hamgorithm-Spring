a = int(input())

for i in range(a) :
    b, c = input().split()
    d = list(c) 
    for j in range(len(d)) :
        for k in range(int(b)) :
            print(d[j], end='')
    print()
            
            
