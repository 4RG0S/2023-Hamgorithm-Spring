#include <stdio.h>
#include <math.h>
int main() {
	double N, B, M, sum = 0;
	int year = 0, ret;
	while (scanf("%lf%lf%lf", &N, &B, &M) != -1) {
		year = 0;
		while (N <= M) {
			N += N * B / 100.f;
			year++;
		}
		printf("%d\n", year);
	}
	return 0;

}