# union find 알고리즘

import sys
input = sys.stdin.readline

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    
    return parent[x]

def union(parent, a, b, know_truth):
    a = find(parent, a)
    b = find(parent, b)

    if a in know_truth and b in know_truth:
        return
    if a in know_truth:
        parent[b] = a
    elif b in know_truth:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

n, m  = map(int, input().split())
know_truth = list(map(int, input().split()))[1 : ]

parties = []
parent = list(range(n + 1))

for _ in range(m):
    party_info = list(map(int, input().split()))
    party_len = party_info[0]
    party = party_info[1:]

    for i in range(party_len - 1):
        union(parent, party[i], party[i + 1], know_truth)
    parties.append(party)

ans = 0
for party in parties:
    for i in range(len(party)):
        if find(parent, party[i]) in know_truth:
            break
    else:
        ans += 1
print(ans)
