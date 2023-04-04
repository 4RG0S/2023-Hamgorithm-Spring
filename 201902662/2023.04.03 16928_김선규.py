from collections import deque
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    dic = {i:0 for i in range(101)}
    visit = {i:False for i in range(101)}
    for _ in range(n+m):
        x, y = map(int, input().split())
        dic[x] = y
    
    st = deque([(1,0)])
    m = 100
    while st:
        v, n = st.popleft()
        if v == 100:
            m = min(m, n)
            continue
        
        for i in range(1,7):
            nv = v + i
            if nv > 100: continue
            if visit[nv]: continue
            visit[nv] = True
            if dic[nv]:
                st.append((dic[nv], n+1))
            else:
                st.append((nv, n+1))
        
    print(m)
    
if __name__ == '__main__':
    main()