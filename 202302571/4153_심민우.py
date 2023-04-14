length = list(map(int,input().split()))

while length[0] != 0:
    length.sort()
    if length[0] * length[0] + length[1] * length[1] == length[2] * length[2]:
        print("right")
    else:
        print("wrong")
    
    length = list(map(int,input().split()))