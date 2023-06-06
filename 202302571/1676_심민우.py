n = int(input())

tot = 0
while n>=5:
    n//=5
    tot +=n

print(tot)