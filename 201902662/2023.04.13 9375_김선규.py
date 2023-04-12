import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        dic = {}
        for i in range(n):
            a, b = input().split()
            try: dic[b] += 1
            except: dic[b] = 1
        
        c = 1
        for i in dic:
            c *= (dic[i] +1)
        print(c-1)
        
if __name__ == "__main__":
    main()