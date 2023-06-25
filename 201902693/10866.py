import sys
input = sys.stdin.readline
n = int(input())
deque = []
for i in range(n) :
    cmd = list(input().split())
    if cmd[0] == 'push_front' :
        deque = [int(cmd[1])] + deque
    if cmd[0] == 'push_back' :
        deque.append(int(cmd[1]))
    if cmd[0] == 'pop_front' :
        if len(deque) == 0 :
            print(-1)
        else :
            print(deque[0])
            del deque[0]
    if cmd[0] == 'pop_back' :
        if len(deque) == 0 :
            print(-1)
        else :
            print(deque[-1])
            del deque[-1]
    if cmd[0] == 'size' :
        print(len(deque))
    if cmd[0] == 'empty' :
        if len(deque) == 0 :
            print(1)
        else :
            print(0)
    if cmd[0] == 'front' :
        if len(deque) == 0 :
            print(-1)
        else :
            print(deque[0])
    if cmd[0] == 'back' :
        if len(deque) == 0 :
            print(-1)
        else :
            print(deque[-1])    