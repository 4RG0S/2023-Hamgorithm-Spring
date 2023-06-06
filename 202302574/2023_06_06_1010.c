#include<stdio.h>
int main() {
	int num, N, K;
	long long c[30][30] = { 0, };
	for (int i = 1; i < 30; i++) {
		c[i][0] = 1;
		c[i][i] = 1;
	}
	for (int i = 2; i < 30; i++) {
		for (int j = 1; j < i; j++) {
			c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
		}
	}
	scanf("%d", &num);
	for (int i = 0; i < num; i++) {
		scanf("%d%d", &K, &N);//(N,K) = (N-1,K-1)+(N-1,K)
		printf("%lld\n", c[N][K]);
	}
}