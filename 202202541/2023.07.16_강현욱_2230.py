x,y = map(int, input().split())
ls=[]
for _  in range(x):
    ls.append(int(input()))
ls.sort()
#투포인터쓰려면 정렬하는게 편한건가요?
start=0
end=1
rs=0
sub=0
while True:
    if(start==x or end==x):
        break
        #st점이 끝까지 가거나 end가 끝까지 가면 브레이크
    sub=ls[end]-ls[start]
    if(sub>y):
         start+=1
         if(sub<=rs or rs==0):
                rs=sub
    elif(sub<y):
        end+=1
    elif(sub==y):
        rs=sub
        break
print(rs)




    


