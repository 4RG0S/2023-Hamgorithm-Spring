import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    
    # 부모 노드를 저장하는 parent
    # 높이를 저장하는 rank
    parent = [i for i in range(n)]
    rank = [1 for _ in range(n)]
    
    # x가 어떤 집합에 속하는지 찾음
    def find(x):
        if x == parent[x]:
            return x
        
        parent[x] = find(parent[x])
        return parent[x]
    
    # a와 b의 parent를 찾아 하나의 집합으로 만듦
    # union by rank를 사용하여 시간복잡도를 줄임
    def union(a, b):
        a, b = find(a), find(b)
        
        if rank[a] < rank[b]:
            a, b = b, a
            
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
    
    # a와 b가 사이클이 생기려면
    # a와 b가 같은 집합에 속할 때 둘을 연결하면 사이클이 생김
    num = 0
    for i in range(m):
        a, b = map(int, input().split())
        if find(parent[a]) == find(parent[b]):
            num = i+1
            break
        union(a, b)    
    print(num)
    
if __name__ == '__main__':
    main()