import sys

def main():
    n = int(sys.stdin.readline())
    log = dict() # key: 이름, value: 출입 여부

    for i in range(n):
        name, el = sys.stdin.readline().split()
        if el == 'enter': # 출근
            log[name] = True
        elif el == 'leave': # 퇴근
            del log[name]
    # 출력, 역순 정렬
    print('\n'.join(sorted(list(log.keys()), reverse=True))) 

if __name__ == "__main__":
    main()
