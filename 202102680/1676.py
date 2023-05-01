a = int(input())

mux = 1

for i in range(1,a+1):
    mux *= i

ans = str(mux)
count = 0
o = -1

while ans[o] == "0" and len(ans) != -o:
    count += 1
    o -= 1

print(count)