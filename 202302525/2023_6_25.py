n = int(input())
tree = list(map(int, input().split()))
k = int(input())
cnt = 0

def dfs(r):
    tree[r] = -2  #현재노트 체크

    for i in tree:
        if i == r:  #현재 노드를 부모로 가지는 노드를 향해 재귀
            dfs(tree.index(i))

dfs(k)

for i in range(len(tree)):
    if tree[i] != -2 and i not in tree:  #체크된 노드 아니고, 자신이 극소라면
        cnt += 1

print(cnt)