from sys import stdin
N, M = map(int, stdin.readline().split())
emeqh = set()
emeqhwkq = set()

for _ in range(N):
    emeqh.add(stdin.readline().rstrip())
    
for _ in range(M):
    emeqhwkq.add(stdin.readline().rstrip())

emeqhwkq = sorted(list(emeqh&emeqhwkq))
print(len(emeqhwkq), *emeqhwkq, sep='\n')
