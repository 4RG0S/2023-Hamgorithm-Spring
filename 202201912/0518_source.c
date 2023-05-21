#include <stdio.h>

int main() {
    int n, k = 0, time = 0;
    scanf("%d", &n);
    while (1) {
        k++;
        if (n == 0) break;
        if (n < k) k = 1;
        n -= k;
        time++;
    }
    printf("%d\n", time);
    return 0;
}