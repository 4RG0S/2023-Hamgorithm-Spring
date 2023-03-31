a = int(input())
new_str = ""
for _ in range(a) :
    n, string = input().split()
    for i in string :
        print(i * int(n), end = '')
    print()