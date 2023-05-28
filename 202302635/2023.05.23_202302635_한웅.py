N = int(input())
line = 1
count = 1

if N == 1 :
       print(count)
else :
       while N > line :
              line += count *6
              count += 1
       print(count)