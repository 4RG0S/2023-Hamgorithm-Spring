N = int(input())

count =0
for i in range(N):
    word = input()
    check=[]
    for elem in word:
        if elem not in check:
            check.append(elem)
        else:
            if elem == check[-1]:
                continue
            else:
                count -=1
                break
    count +=1
print(count)