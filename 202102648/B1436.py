import sys
input = sys.stdin.readline

n = int(input())

s = 666
cnt=0

while True:
    if '666' in str(s):
        cnt +=1
    if cnt == n:
        print(s)
        break
    s += 1

