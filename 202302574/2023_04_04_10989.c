#include<stdio.h>
int main() {
    int arr[10001] = { 0, };
    int num, i, j, temp;
    scanf("%d", &num);
    for (i = 0; i < num; i++) {
        scanf("%d", &temp);
        arr[temp]++;
    }
    for (i = 1; i < 10001; i++) {
        if (arr[i] == 0) continue;
        for (j = 0; j < arr[i]; j++) {
            printf("%d\n", i);
        }
    }
}