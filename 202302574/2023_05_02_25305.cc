#include<stdio.h>
int main() {
    int num, cutNum, cutLine, i, j, Temp;
    scanf("%d %d", &num, &cutNum);

    int arr[1000] = { 0 };
    for (i = 0; i < num; i++) {
        scanf("%d", &Temp);
        arr[i] = Temp;
    }

    for (i = 0; i < num; i++) {
        for (j = 0; j < num - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = temp;
            }
        }
    }
    printf("%d", arr[num - cutNum]);
}