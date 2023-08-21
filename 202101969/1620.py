import sys

epoch, q = map(int, sys.stdin.readline().split())
re = {}
for i in range(epoch):
    name = sys.stdin.readline()
    re[i+1] = name[:-1]

rever = {v:k for k,v in re.items()}
for i in range(q):
    an = sys.stdin.readline()
    if 48 <= ord(an[0]) <= 57:
        print(re[int(an)])
    else:
        print(rever[str(an[:-1])])
