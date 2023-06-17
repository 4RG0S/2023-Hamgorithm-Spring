# import numpy as np

n = int(input())
scores = list(map(int, input().split(" ")))
# scores = np.array(scores)
# max_score = np.max(scores)
# print(scores)
max_score = max(scores)
for i in range(n):
    scores[i] = scores[i] / max_score * 100
# new_scores = scores / max_score * 100

print(sum(scores)/n)
