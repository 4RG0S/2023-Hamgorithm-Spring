import sys

count = 0

while count < 3:
    n = int(input())
    a = 0

    for i in range(n):
        a += int(sys.stdin.readline())

    if a == 0:
        print('0')
    
    elif a < 0:
        print('-')

    else:
        print('+')

    count += 1