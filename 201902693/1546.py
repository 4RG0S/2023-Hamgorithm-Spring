n = int(input())
input_list = list(map(float, input().split()))
max_score = max(input_list)
for i in range(n) :
    input_list[i] = (input_list[i] / max_score) * 100
print(sum(input_list) / n)