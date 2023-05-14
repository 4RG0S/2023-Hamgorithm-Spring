#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int isPrime(long long N) {
    if (N == 1) {
        return 0;
    }
    if (N == 2 || N == 3) {
        return 1;
    }
    int this = 1;
    for (int i = 2; i <= sqrt(N); i++) {
        if (N % i == 0) {
            this = 0;
            break;
        }
    }
    return this;
}

int main() {
    int test;
    scanf("%d", &test);

    while (test--) {
        long long N;
        scanf("%lld", &N);

        if (N == 0 || N == 1 || N == 2) {
            printf("2\n");
        }
        else {
            if (N % 2 == 0) {
                N++;
            }
            while (!isPrime(N)) {
                N += 2;
            }
            printf("%lld\n", N);
        }

    }
    return 0;
}