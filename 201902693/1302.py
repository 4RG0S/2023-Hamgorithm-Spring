from collections import Counter

n = int(input())
lst = []
for i in range(n) :
    lst.append(input())
cnt = Counter(lst)
count = cnt.most_common()
result = []
for i in range(len(count)) :
    if count[0][1] == count[i][1] :
        result.append(count[i])
result.sort()
print(result[0][0])