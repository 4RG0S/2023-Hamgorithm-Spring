arr = []

for i in range(1, 31):
    arr.append(i)

for j in range(28):
    arr.remove(int(input()))

for k in range(len(arr)):
    print(arr[k])