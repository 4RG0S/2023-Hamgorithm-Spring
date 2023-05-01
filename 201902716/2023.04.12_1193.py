def main():
    x = int(input())
    k = 1
    fraction = []
    
    while(x > k*(k+1)/2):
        k += 1    
        
    for i in range(k):
        fraction.append("%d/%d" %(k-i, i+1))
    
    if k % 2 == 0:
        print(fraction[int(k-(x-(k-1)*k/2))])
    else:
        print(fraction[int(x-(k-1)*k/2-1)])
        
if __name__ == '__main__':
    main()
