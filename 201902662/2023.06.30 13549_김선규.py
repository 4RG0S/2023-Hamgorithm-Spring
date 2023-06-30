from collections import deque
Inf = float('inf')

def main():
    n, k = map(int, input().split())
    # 목적지까지의 거리를 무한하게 설정
    dist = [Inf for i in range(100001)]
    dist[n] = 0
    
    que = deque([(n, 0)])
    while que:
        x, v = que.popleft()
        
        # 값의 반복 계산을 막기 위해 계산하여 변수에 저장
        a, b, c, nv = 2 * x, x-1, x+1, v+1
        #  순간이동하여 2배의 위치로 이동
        if 0 <= a <= 100000 and dist[a] > v:
            dist[a] = v
            que.append((a, v))
        # -1만큼 이동
        if 0 <= b <= 100000 and dist[b] > nv:
            dist[b] = nv
            que.append((b, nv))
        # +1만큼 이동
        if 0 <= c <= 100000 and dist[c] > nv:
            dist[c] = nv
            que.append((c, nv))

    print(dist[k])
    
if __name__ == "__main__":
    main()