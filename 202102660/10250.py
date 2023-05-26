# 호수가 몫, 나머지가 층

case = int(input())

while case>0:
    case -= 1
    h, w, n = map(int, input().split(" "))
    ho = (n//h+1) if n%h!= 0 else n//h
    floor = (n%h) if n%h!= 0 else h
    print(f"{floor}{ho:02d}")