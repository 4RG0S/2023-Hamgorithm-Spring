from collections import deque

T = int(input())

for i in range (T):
    func = input()
    num = int(input())
    deq = deque(input()[1:-1].split(','))
    flag = 0
    
    if num == 0:
        deq = []
    
    for j in func:
        if j == 'R':
            flag += 1
        elif j == 'D':
            if len(deq) == 0:
                print("error")
                break
            if flag%2 == 0:
                deq.popleft()
            else:
                deq.pop()
    else:
        if flag%2 == 1:
            deq.reverse()
        print('[' + ','.join(deq) + ']')
