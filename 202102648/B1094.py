x = int(input())

st = 64
cnt =0
while x>0:
    if st>x:
        st //=2
    else:
        cnt += 1
        x -= st
print(cnt)