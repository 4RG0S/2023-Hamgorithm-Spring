import sys

def find_num(n):
    global ids
    for _ in range(n):
        ids.append(str(input()))
    for i in range(1, len(ids[0]) + 1):
        results = []
        for j in range(n):
            if ids[j][-i:] in results:
                break
            else:
                results.append(ids[j][-i:])
        if len(results) == n:
            print(i)
            break

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    ids = []
    find_num(N)
