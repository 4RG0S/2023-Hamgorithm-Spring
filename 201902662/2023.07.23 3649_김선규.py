import sys
input = sys.stdin.readline

def main():
    while True:
        try:
            x, n = int(input()) * 10000000, int(input())
            li = sorted([int(input()) for _ in range(n)])
            
            # 모든 경우에 대해 순회하며 이진 탐색을 수행한다.
            # index i 인 경우 구해야 되는 값t에는 x와 li[i]의 차이를 저장한다.
            # 이진 탐색을 수행하며 t와 같은 값이 있는지 확인한다.
            # 있다면 yes를 출력하고 없다면 danger를 출력한다.
            # 처음 발견하면 가장 두 값이 가장 크기 때문에 바로 종료한다.
            def search():
                for i in range(n-1):
                    t = x - li[i]
                    left, right = i+1, n-1
                    while left <= right:
                        mid = (left+right)//2
                        if li[mid] == t:
                            print("yes", li[i], li[mid])
                            return
                        elif li[mid] < t:
                            left = mid+1
                        else:
                            right = mid-1
                print("danger")
            
            search()
        except:
            break
        
if __name__ == "__main__":
    main()