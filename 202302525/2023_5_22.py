n = int(input())

table = list(map(int, input().split()))
table.sort()

print(table[0] * table[-1])