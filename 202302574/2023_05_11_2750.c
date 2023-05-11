#include<stdio.h>
int main() {
    int arr[2001] = { 0, };
    int num, temp;
    scanf("%d", &num);
    for (int i = 0; i < num; i++) {
        scanf("%d", &temp);
        arr[temp+1000]++;
    }
    for (int i = 0; i < 2001; i++) {
        if (arr[i]) printf("%d\n", i-1000);
    }
}