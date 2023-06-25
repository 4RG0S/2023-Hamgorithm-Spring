#include<stdio.h>

int main() {
    int L, S[1001] = { 0, }, n, temp;
    scanf("%d", &L);
    for (int i = 1; i <= L; i++) scanf("%d", &S[i]);
    scanf("%d", &n);
    for (int i = L; i > 0; i--)
        for (int j = 0; j < i; j++)
            if (S[j] > S[j + 1]) {
                temp = S[j];
                S[j] = S[j + 1];
                S[j + 1] = temp;
            }
    for (int i = 0; i <= L; i++) {
        if (S[i] > n) {
            printf("%d", (n - S[i - 1]) * (S[i] - n) - 1);
            return 0;
        }
        else if (S[i] == n) {
            printf("0");
            return 0;
        }
    }
}