# 입력이 최대 10000줄이 들어오기 때문에 
# sys.stdin.readline을 이용하지 않으면 시간초과
import sys
input = sys.stdin.readline
n = int(input())

st = []
for i in range(n) :
    cmd = list(input().split())
    if cmd[0] == 'push' :
        st.append(int(cmd[1]))
    if cmd[0] == 'top' :
        if len(st) == 0 :
            print(-1)
        else :    
            print(st[-1])
    if cmd[0] == 'size' :
        print(len(st))
    if cmd[0] == 'empty' :
        if len(st) == 0 :
            print(1)
        else :
            print(0)
    if cmd[0] == 'pop' :
        if len(st) == 0 :
            print(-1)
        else :
            print(st.pop())
            
