N, kjm, ihs = map(int ,input().split())
result = 0
while kjm != ihs:
    kjm -= kjm // 2
    ihs -= ihs // 2
    result += 1
print(result)
