N = int(input())
N_list = list(map(int, input().split()))
src = [0] * N
result_list = []
for i, val in enumerate(N_list):
    tmp = val
    person = 0
    for j in range(N):
        if person == tmp and src[j] == 0:
            src[j] = i+1
            break
        elif src[j] == 0:
            person += 1
print(*src)
