#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        char arr[100] = { 0 };
        int f = 0, s = 0, k = 1, ten = 1;;
        scanf("%s", arr);

        for (int i = 2; i >= 0; i--) {
            f += (arr[i] - 65) * k;
            k = k * 26;
        }

        for (int i = 7; i >= 4; i--, ten *= 10) {
            s += (arr[i] - 48) * ten;;
        }

        if (abs(f - s) <= 100) {
            printf("nice\n");
        }
        else {
            printf("not nice\n");
        }

    }
    return 0;
}
