import math

S = list(input())
a_count = S.count('a')
result = math.inf
posit = 0

while posit < len(S):
  right = posit + a_count
  if right > len(S):
    temp = S[posit:len(S)] + S[:right-len(S)]
  else:
    temp = S[posit:right]
  result = min(result, temp.count('b'))
  posit += 1
print(result)
