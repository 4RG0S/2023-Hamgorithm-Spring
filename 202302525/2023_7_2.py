#여름방학 '햄'고리즘 1주차(1)

from collections import deque

n = int(input())
m = int(input())
cnt = -1 #1을 포함하여 카운트 할 것이기 때문에 -1로 설정
tree = [[] for _ in range(n)] #트리(노드들)
visited = [False for _ in range(n)] #방문표시를 위한 배열
dfs_stack = deque([])  #탐색을 위한 큐

#트리 그리기
for _ in range(m):
    x, y = map(int, input().split())

    tree[x-1].append(y)
    tree[y-1].append(x)


#1부터 탐색 시작
dfs_stack.append(1)


while dfs_stack:
    k = dfs_stack.popleft()

    visited[k-1] = True #방문처리

    while tree[k-1]:
        i = tree[k-1][0]

        if visited[i-1] == True:
            continue
        
        else:
            tree[k-1].remove(i) #간선제거
            tree[i-1].remove(k) 

            dfs_stack.append(i) #큐에 push

for i in visited: #방문한 노드 카운트
    if i == True:
        cnt += 1


print(cnt)