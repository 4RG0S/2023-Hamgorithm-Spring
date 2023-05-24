#include<stdio.h>

int main() {
    long long num, temp0, temp1 = 1, temp2, temp3 = 1;
    scanf("%lld", &num);
    if (num == 1 || num == 2) printf("1");
    else {
        for (int i = 0; i < num - 2; i++) {
            temp0 = temp1;
            temp1 = temp3;
            temp2 = temp0;
            temp3 = temp1 + temp2;
        }
        printf("%lld", temp3);
    }
}