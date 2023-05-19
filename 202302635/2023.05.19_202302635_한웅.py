s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
N, B = map(int, input().split())
a = ''

while N != 0:
    a += str(s[N % B]) 
    N //= B
    
print(a[::-1])