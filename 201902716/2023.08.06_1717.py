import sys

def find_mom(mom, x): # 엄마 찾기
    if mom[x] != x:
        mom[x] = find_mom(mom, mom[x])
    return mom[x]

def union(mom, a, b): # 너 내 엄마가 되라
    a = find_mom(mom, a)
    b = find_mom(mom, b)

    if a != b:
        mom[b] = a

def main():
    n, m = map(int, sys.stdin.readline().split())
    mom = [i for i in range(n + 1)]

    for _ in range(m):
        op, a, b = map(int, sys.stdin.readline().split())
        if op == 0: # 합집합 연산
            union(mom, a, b)
        else:  # 같은 집합인지 확인 연산
            if find_mom(mom, a) == find_mom(mom, b):
                print("YES") # 엄마 같으면
            else:
                print("NO") # 엄마 다르면

if __name__ == "__main__":
    main()
