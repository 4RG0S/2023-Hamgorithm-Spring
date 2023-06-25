n = int(input())

arr = list(map(int, input().split()))

c = int(input())

count = 0

for i in range(n):
    a = arr[i] / c

    if  a == int(a):
        count += c*a

    elif a < 1:
        count += c

    else:
        count += c*(int(a)+1)

print(int(count))