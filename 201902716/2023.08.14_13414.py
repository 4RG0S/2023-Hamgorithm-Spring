import sys

def main():
    k, l = map(int, sys.stdin.readline().split())
    sugang = dict()

    for i in range(l):
        snum = sys.stdin.readline().strip()
        if snum in sugang.keys(): # 이미 있으면
            del sugang[snum]
            sugang[snum] = True # 뒤로 보내기
        else: # 없으면
            sugang[snum] = True # 추가
    # 출력
    print('\n'.join(list(sugang.keys())[:k]))

if __name__ == "__main__":
    main()
