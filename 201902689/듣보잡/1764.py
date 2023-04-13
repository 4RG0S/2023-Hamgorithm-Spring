n, m = map(int, input().split(' '))

no_hear_lst = []
no_look_lst = []

for i in range(n):
    no_hear_lst.append(input())
for j in range(m):
    no_look_lst.append(input())

intersection = list(set(no_hear_lst) & set(no_look_lst))
intersection.sort()
print(len(intersection))
for name in intersection:
    print(name)