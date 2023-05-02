n = int(input())
score = [int(i) for i in input().split()]
score.sort()
list = []
a = 0

for i in range(n):
    list.append(score[i]/score[n-1]*100)

for i in range(n):
    a = a + list[i]

print(a/n)