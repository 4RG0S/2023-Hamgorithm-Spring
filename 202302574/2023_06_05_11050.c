#include<stdio.h>
int factorial(int N) {
    int result = 1;
    for (int i = 1; i <= N; i++) {
        result *= i;
    }
    return result;
}
int main() {
    int N, K;
    scanf("%d%d", &N, &K);
    printf("%d", factorial(N) / (factorial(K) * factorial(N - K)));
}