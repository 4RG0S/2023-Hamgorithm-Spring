N_list = []
max_ = 0
for _ in range(int(input())):
    country, student, score = map(int, input().split())
    N_list.append([score, country, student])
    if max_ < country:
        max_ = country
res = []
c_dict = {i:0 for i in range(1,max_+1)}
for i in reversed(sorted(N_list)):
    c_dict[i[1]] += 1
    if c_dict[i[1]] > 2:
        continue
    res.append([i[1],i[2]])
    if len(res) == 3:
        break
for i in res:
    print(i[0], i[1])
