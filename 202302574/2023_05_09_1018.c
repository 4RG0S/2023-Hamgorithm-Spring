#include <stdio.h>
int main() {
    int row, col;
    char array[50][51];
    int min = 32;

    scanf("%d%d", &row, &col);

    for (int i = 0; i < row; i++) {
        scanf("%s", array[i]);
    }

    for (int i = 0; i < row - 7; i++) {
        for (int j = 0; j < col - 7; j++) {
            int count = 0;
            for (int k = i; k < i + 8; k++) {
                for (int l = j; l < j + 8; l++) {
                    count += (k + l) % 2 == 1 ^ array[k][l] == 'B';
                    /*
                    Case 1. k와 l의 홀짝이 다를 때(즉, arrWB에서 B위치),
                        ㄱ. B일 경우 => x
                        ㄴ. W일 경우 => count++
                    */

                    /*
                    Case 2. k와 l의 홀짝이 같을 때(즉, arrWB에서 W위치),
                        ㄱ. B일 경우 => count++
                        ㄴ. W일 경우 => x
                    */
                }
            }
            count = 64 - count < count ? 64 - count : count;
            min = count < min ? count : min;
        }
    }
    printf("%d", min);
}