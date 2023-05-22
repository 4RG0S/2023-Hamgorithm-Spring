#include<stdio.h>
int main() {
    int num, temp, min = 1000001, max = 1;
    scanf("%d", &num);
    for (int i = 0; i < num; i++) {
        scanf("%d", &temp);
        if (temp < min) min = temp;
        if (temp > max) max = temp;
    }
    printf("%d", min * max);

}