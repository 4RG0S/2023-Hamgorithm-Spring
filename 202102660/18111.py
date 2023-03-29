import sys

N, M, B = map(int, input().split())
ground = [
    list(map(int, input().split()))
    for _ in range(N)
]
height = 0
time = sys.maxsize

for h in range(257):
    to_dig = 0
    to_build = 0
    for l in ground:
        for item in l:
            if (item <= h):
                # 쌓아야됨.
                to_build += (h-item)
            else :
                # 파야됨
                to_dig += (item-h)
    if (to_dig+B) < to_build:
        continue

    
    tmp = (to_dig*2)+ to_build
    if time >= tmp:
        time = tmp
        height = h

print(f'{time} {height}')
    
