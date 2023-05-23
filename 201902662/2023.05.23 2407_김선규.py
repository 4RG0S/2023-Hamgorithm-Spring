def main():
    n, m = list(map(int, input().split()))
    nli = [i for i in range(n, n-m, -1)]
    mli = [i for i in range(m, 0, -1)]
    for i in range(m):
        for j in range(m):
            if mli[j] != 1 and nli[i] % mli[j] == 0:
                nli[i] = int(nli[i] / mli[j])
                mli[j] = 1
    
    nMul = 1
    mMul = 1
    for i in range(m):
        nMul *= nli[i]
        mMul *= mli[i]
    
    print(nMul//mMul)
    
if __name__ == "__main__":
    main()