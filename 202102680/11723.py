import sys
l = set()
n = int(input())

for _ in range(n):
    line = sys.stdin.readline().rstrip().split()
    if line[0] == 'all' or line[0] == 'empty':
        if line[0] == 'all':
            l = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        elif line[0] == 'empty':
            l = set()
    else:
        num = int(line[1])
        if line[0] == 'add':
            if l.intersection(set([num])):
                continue
            else:
                l.add(num)
        elif line[0] == 'remove':
            if l.intersection(set([num])):
                l.remove(num)
            else:
                continue
        elif line[0] == 'check':
            if l.intersection(set([num])):
                print(1)
            else:
                print(0)
        elif line[0] == 'toggle':
            if l.intersection(set([num])):
                l.remove(num)
            else:
                l.add(num)


