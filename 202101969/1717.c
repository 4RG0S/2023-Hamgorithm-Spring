# #include <stdio.h>
# #include <stdbool.h>
int parent[1000000];

int Find(int x){
    if (x == parent[x]){
        return x;
    }
    else{
        return parent[x] = Find(parent[x]);
    }
}

void Union(int x, int y){
    x = Find(x);
    y = Find(y);

    if (x==y){
        return;
    }
    if(x < y){
        parent[y] = x;
    }
    else{
        parent[x] = y;
    }
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    for(int i = 0; i<=n; i++){
        parent[i] = i;
    }

    for(int i=0; i<m; i++){
        int a,b,c;
        scanf("%d %d %d",&a,&b,&c);
        if (a ==0){
            Union(b,c);
        }
        else{
            int B,C;
            B = Find(b);
            C = Find(c);
            if (B == C){
                printf("YES \n");
            }
            else{
                printf("NO \n");
            }
        }
    }
    return 0;
}