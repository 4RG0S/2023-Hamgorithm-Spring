#include<stdio.h>
int main() {
    int result = 666;
    int i, count = 0;
    int n;
    scanf("%d", &n);
    while (1) {
        for (i = result; i; i /= 10) {
            if (i % 1000 == 666) {
                count++;
                break;
            }
        }
        if (count == n) {
            printf("%d", result);
            return 0;
        }
        result++;
    }
}