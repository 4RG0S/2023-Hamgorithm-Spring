a = list(map(int,input().split()))

if sum(a) - max(a) <= max(a) :
    print(2*(sum(a) - max(a)) - 1)
else :
    print(sum(a))