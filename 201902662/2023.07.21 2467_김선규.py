def main():
    n = int(input())
    li = list(map(int, input().split()))
    
    # 모든 용액에 대해 특성값이 0에 가깝하는 두 용액을 찾는다.
    # 이진탐색을 통해 두 용액의 특성값이 작은 경우 저장한다.
    left, right, m = 0, 0, 2000000000
    for i in range(n-1):
        start, end = i + 1, n - 1
        while start <= end:
            center = (start + end) // 2
            tmp = li[i] + li[center]
            
            if abs(tmp) < m:
                m = abs(tmp)
                left, right = i, center
            
            if tmp < 0:
                start = center + 1
            else:
                end = center - 1
    
    print(li[left], li[right])
    
if __name__ == "__main__":
    main()