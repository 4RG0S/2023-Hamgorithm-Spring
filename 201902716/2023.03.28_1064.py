def main():
    p = []
    xa, ya, xb, yb, xc, yc = map(float, input().split())
    
    p.append((abs(xa-xb)**2 + abs(ya-yb)**2)**0.5)
    p.append((abs(xb-xc)**2 + abs(yb-yc)**2)**0.5)
    p.append((abs(xc-xa)**2 + abs(yc-ya)**2)**0.5)
    answer = (max(p) - min(p))*2
    
    if (xa-xb)*(ya-yc) == (xa-xc)*(ya-yb):
        print(-1.0)
    else:
        print(answer)

if __name__ == '__main__':
    main()
    
