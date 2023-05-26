#include<stdio.h>
int main() {
	//  N*(2M+N-1) = 2*S 를 만족시키는 최소의 N을 구하시오. 
	int S, N, i, j, k;
	scanf("%d%d", &S, &N);
	for (i = N; i <= 100; i++) {
		for (j = S/i+1; j >= 0; j--) {
			if (i * (2 * j + i - 1) == 2 * S) {
				for (k = 0; k <i; k++) {
					printf("%d ", j+k);
				}
				return 0;
			}
		}
	}
	printf("-1");
}