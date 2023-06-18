N = int(input())
ms = 0
for i in range(N) :
    i_list = list(map(int,str(i)))
    if sum(i_list) + i == N :
        if ms == 0 :    
            ms = i
            break
        
    
print(ms)

