import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    poketmon = dict() # key: 번호, value: 포켓몬 이름
    nums = dict() # key: 포켓몬 이름, value: 번호

    for i in range(1, N + 1):
        poketmon[i] = sys.stdin.readline().strip()
        nums[poketmon[i]] = i

    for _ in range(M):
        s = sys.stdin.readline().strip()
        if s.isdigit(): # 숫자면
            print(poketmon[int(s)]) # 번호로 출력
        else: # 문자면
            print(nums[s]) # 포켓몬 이름으로 출력

if __name__ == "__main__":
    main()
