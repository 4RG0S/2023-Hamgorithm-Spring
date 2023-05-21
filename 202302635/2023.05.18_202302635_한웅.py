N, B = list(input().split())

def ASCII(a) :
    if '0' <= a <= '9' :
        return int(a)
    return ord(a) - 55


T = 0
for i in range(len(N)) :
    T += ASCII(N[i]) * (int(B) ** (len(N)-i-1))

print(T) 