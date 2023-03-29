n = int(input())
stack = []
answer = []
cur = 1
a = 1
for i in range(n):
    inp = int(input())
    while cur <= inp:
        stack.append(cur)
        answer.append("+")
        cur += 1

    if stack[-1] == inp:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        a = 0
        break

if a == 1:
    for elem in answer:
        print(elem)