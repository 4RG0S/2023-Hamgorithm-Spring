#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a[20], b[20], i, t = 0, m = 0, k = 0;
    for (i = 1; i <= 9; i++) {
        scanf("%d", &a[i]);
    }
    for (i = 1; i <= 9; i++) {
        scanf("%d", &b[i]);
    }
    for (i = 1; i <= 9; i++) {
        t = t + a[i];
        if (t > m) {
            printf("Yes");
            return 0;
        }
        else {
            k++;
        }
        m = m + b[i];
    }
    if (k == 9) {
        printf("No");
    }
    return 0;
}