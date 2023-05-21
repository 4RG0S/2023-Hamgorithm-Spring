from collections import deque
import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        a, b = list(map(int, input().split()))
        visit = [True] * 10000
        
        que = deque([(a, "")])
        while que:
            e, v = que.popleft()
            if e == b:
                print(v)
                break
            
            d = 2 * e % 10000
            ds = "".join([v,"D"])
            if visit[d]:
                que.append((d, ds))
                visit[d] = False
            
            s = e-1
            ss = "".join([v,"S"])
            if s == -1:
                s = 9999
            if visit[s]:
                que.append((s, ss))
                visit[s] = False
            
            l = e%1000*10+int(e/1000)
            ls = "".join([v,"L"])
            if visit[l]:
                que.append((l, ls))
                visit[l] = False
            
            r = int(e/10)+e%10*1000
            rs = "".join([v,"R"])
            if visit[r]:
                que.append((r, rs))
                visit[r] = False
            
if __name__ == '__main__':
    main()