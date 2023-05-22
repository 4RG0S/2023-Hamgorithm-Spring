import sys

n = int(sys.stdin.readline())
inp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = []
def cut(x, y, N) :
  color = inp[x][y]
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != inp[i][j] :
        cut(x, y, N//2)
        cut(x, y+N//2, N//2)
        cut(x+N//2, y, N//2)
        cut(x+N//2, y+N//2, N//2)
        return
  if color == 0 :
    result.append(0)
  else :
    result.append(1)

cut(0,0,n)

print(result.count(0))
print(result.count(1))