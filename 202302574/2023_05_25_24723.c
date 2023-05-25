#include<stdio.h>
int main() {
    int num, N = 1;
    scanf("%d", &num);
    for (int i = 0; i < num; i++) {
        N *= 2;
    }
    printf("%d", N);
}