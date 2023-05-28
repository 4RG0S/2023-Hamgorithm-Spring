count=int(input())


roll=[[0]*2 for u in range(count)]
for y in range(count):
    roll[y]=input().split()
    roll[y][0]=int(roll[y][0])
    

roll.sort(key=lambda x:x[0],reverse=False)

for h in range(count):
    print("%d %s"%(roll[h][0],roll[h][1]))






