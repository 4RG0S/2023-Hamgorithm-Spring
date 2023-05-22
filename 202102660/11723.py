import sys

n = int(sys.stdin.readline().strip())
S = set()

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다. 

for i in range(n):
    line = sys.stdin.readline().strip().split()
    
    if len(line) == 1:
        if line[0] == "all":
            for i in range(1, 21):
                S.add(i)
        else:
            S.clear()
    else :
        command, x = line[0], line[1]
        if command == "add":
            S.add(x)
        elif command == "remove":
            S.discard(x)
        elif command =="check":
            print(1 if x in S else 0)
        elif command == "toggle":
            if x in S:
                S.remove(x)
            else :S.add(x)
    
    
 