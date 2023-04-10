from collections import deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    img_a = [[] for i in range(n)]
    img_b = [[] for i in range(n)]
    for i in range(n):
        row = input()
        img_a[i] = list(row)
        img_b[i] = list(row.replace('G','R'))
    
    visit_a = [[False for i in range(n)] for j in range(n)]
    visit_b = [[False for i in range(n)] for j in range(n)]
    
    a, b = 0, 0
    for i in range(n):
        for j in range(n):
            if not visit_a[i][j]:
                que = deque([(i,j)])
                a += 1
                while que:
                    v0, v1 = que.popleft()
                    if visit_a[v0][v1]: continue
                    visit_a[v0][v1] = True
                    if v0-1 >= 0 and img_a[v0][v1] == img_a[v0-1][v1]:
                        que.append((v0-1,v1))
                    if v0+1 < n and img_a[v0][v1] == img_a[v0+1][v1]:
                        que.append((v0+1,v1))
                    if v1-1 >= 0 and img_a[v0][v1] == img_a[v0][v1-1]:
                        que.append((v0,v1-1))
                    if v1+1 < n and img_a[v0][v1] == img_a[v0][v1+1]:
                        que.append((v0,v1+1))
                        
            if not visit_b[i][j]:
                que = deque([(i,j)])
                b += 1
                while que:
                    v0, v1 = que.popleft()
                    if visit_b[v0][v1]: continue
                    visit_b[v0][v1] = True
                    if v0-1 >= 0 and img_b[v0][v1] == img_b[v0-1][v1]:
                        que.append((v0-1,v1))
                    if v0+1 < n and img_b[v0][v1] == img_b[v0+1][v1]:
                        que.append((v0+1,v1))
                    if v1-1 >= 0 and img_b[v0][v1] == img_b[v0][v1-1]:
                        que.append((v0,v1-1))
                    if v1+1 < n and img_b[v0][v1] == img_b[v0][v1+1]:
                        que.append((v0,v1+1))

    print(a, b)
    
if __name__ == '__main__':
    main()