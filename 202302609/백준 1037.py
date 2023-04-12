n = int(input())
divisors = list(map(int, input().split()))

divisors.sort()
result = divisors[0] * divisors[-1]

print(result)
