#include<stdio.h>
int main() {
    char arr[9] = { 0, };
    int count = 0, remain = 0;
    for (int i = 0; i < 8; i++) {
        scanf("%s", arr);
        for (int j = 0; j < 4; j++) {
            if (arr[2 * j + remain] == 'F') count++;
        }
        remain = (remain + 1) % 2;
    }
    printf("%d", count);
}