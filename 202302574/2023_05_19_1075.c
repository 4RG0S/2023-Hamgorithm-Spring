#include<stdio.h>
int main() {
    int num, divisor, i;
    scanf("%d%d", &num, &divisor);
    num = num / 100 * 100;
    for (i = 0; i < 100; i++) {
        if ((num + i) % divisor == 0) break;
    }
    printf("%02d", i);
}