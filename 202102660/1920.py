N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

for b in B:
    flag = False
    s_idx = 0
    f_idx = N-1
    idx = f_idx//2
    while(s_idx<f_idx):
        if b < A[idx]:
            f_idx = idx-1
            idx = (s_idx+f_idx)//2
            continue
        elif b > A[idx]:
            s_idx = idx+1
            idx = (s_idx + f_idx)//2
            continue
        else:
            print(1)
            flag = True
            break
    if flag==False:
        if (s_idx == f_idx) & (b==A[idx]):
            print(1)
        else :
            print(0) = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

for b in B:
    flag = False
    s_idx = 0
    f_idx = N-1
    idx = f_idx//2
    while(s_idx<f_idx):
        if b < A[idx]:
            f_idx = idx-1
            idx = (s_idx+f_idx)//2
            continue
        elif b > A[idx]:
            s_idx = idx+1
            idx = (s_idx + f_idx)//2
            continue
        else:
            print(1)
            flag = True
            break
    if flag==False:
        if (s_idx == f_idx) & (b==A[idx]):
            print(1)
        else :
            print(0)
