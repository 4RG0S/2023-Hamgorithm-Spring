l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
count = 0

while a > 0 or b > 0:
    a = a - c
    b = b - d
    count += 1 

print(l-count)