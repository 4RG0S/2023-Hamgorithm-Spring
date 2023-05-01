#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);

    int q_5 = N/5;
    int r_5 = N%5;
    int count = q_5;
    int flag = 0;
    switch (r_5)
    {
        case 0:
            if (q_5 != 0) {
                flag = 1;
            }
            break;
        case 1:
            if (count > 0) {
                count += 1;
                flag = 1;
            }
            break;
        case 2:
            if (count > 1) {
                count += 2;
                flag = 1;
            }
            break;
        case 3:
            count += 1;
            flag = 1;
            break;
        case 4:
            if (count > 0) {
                count += 2;
                flag = 1;
            }
            break;
    }

    if (!flag){
        count = -1;
    }
    printf("%d", count);

    return 0;
}