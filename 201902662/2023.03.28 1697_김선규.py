def main():
    n, k = list(map(int, input().split()))
    li = [float('inf') for i in range(100001)]
    st = [[n, 0]]
    while st:
        v, d = st.pop(0)
        if v < 0 or v > 100000:
            continue
        if li[v] > d:
            li[v] = d
            st.append([v-1,d+1])
            st.append([v+1,d+1])
            st.append([v*2,d+1])
    print(li[k])
    
if __name__ == '__main__':
    main()