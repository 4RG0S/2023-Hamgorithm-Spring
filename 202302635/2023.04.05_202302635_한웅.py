N , X = map(int,input().split())
List = list(map(int,input().split()))

for i in range(N):
    if List[i] < X :
        print(List[i],end =" ")
