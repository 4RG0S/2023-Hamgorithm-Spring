import sys

n = int(sys.stdin.readline())
arr = [0]

for i in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        a = len(arr)
        arr.append(x)

        while a != 1 and x < arr[a//2]:
            arr[a] = arr[a//2]
            a = a//2

        arr[a] = x

    else:
        if len(arr) == 1:
            print(0)

        elif len(arr) == 2:
            print(arr[1])
            arr.pop()

        elif len(arr) == 3:
            min = arr[1]
            arr[1] = arr[len(arr)-1]
            arr.pop()

            print(min)

        else:
            min = arr[1]
            arr[1] = arr[len(arr)-1]
            arr.pop()

            p = 1
            c = 0

            while True:
                c = 2*p

                if c+1 <= len(arr)-1 and arr[c] > arr[c+1]:
                    c += 1

                if c > len(arr) or arr[c] > arr[p]:
                    break

                arr[p], arr[c] = arr[c], arr[p]
                p = c

            print(min)