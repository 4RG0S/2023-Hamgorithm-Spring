n = int(input())
arr = [0 for i in range(26)]

print(arr)

for i in range(n):
    st = list(input())
    first = ord(st[0]) - 97

    arr[first] += 1

for j in range(26):
    if arr[j] >= 5:
        print(chr(j+97), end ='')