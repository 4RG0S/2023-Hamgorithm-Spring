#include<stdio.h>
int main(){
    int a, b, c, d, e, f;
    scanf("%d%d%d%d%d%d", &a, &b, &c, &d, &e, &f);
    
    printf("%d %d", (c*e-b*f)/(a*e-b*d), (c*d-a*f)/(b*d-a*e));
}