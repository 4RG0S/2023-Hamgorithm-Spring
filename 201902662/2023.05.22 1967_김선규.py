from collections import deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    tree = [[] for _ in range(n+1)]
    for i in range(n-1):
        parent, child, value = list(map(int, input().split()))
        tree[parent].append((child, value))
        tree[child].append((parent, value))

    def dfs(num):
        maxNode = (0, 0)
        visit = [True for _ in range(n+1)]
        visit[num] = False
        stack = deque([(num, 0)])
        while stack:
            parent, value = stack.pop()
            
            if maxNode[1] < value:
                maxNode = (parent, value)
                
            for child in tree[parent]:
                if visit[child[0]]:
                    stack.append((child[0], value + child[1]))
                    visit[child[0]] = False
        return maxNode
    
    print(dfs(dfs(1)[0])[1])
    
if __name__ == "__main__":
    main()