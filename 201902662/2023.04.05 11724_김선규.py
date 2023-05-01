from collections import deque
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    dic = {i:deque() for i in range(1,n+1)}
    visit = [False for i in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        dic[u].append(v)
        dic[v].append(u)
    
    num = 0
    st = deque()
    for i in range(1,n+1):
        if visit[i]: continue
        num += 1
        st.append(i)
        while st:
            u = st.popleft()
            if visit[u]: continue
            visit[u] = True
            for v in dic[u]:
                st.append(v)
    print(num)
    
if __name__ == '__main__':
    main()