N = int(input())

ls = list(map(int,input().split()))
max = ls[0]
min = ls[0]

for i in ls[1:]:
    if i > max :
        max = i
    elif i < min :
        min = i 
print(min,max)