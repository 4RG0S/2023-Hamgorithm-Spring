#include <stdio.h>
int f(int a, int b) {
	if (!(a % b)) return b;
	return f(b, a % b);
}
int main() {
	int N, a, b;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d %d", &a, &b);
		printf("%d\n", a * b / f(a, b));
	}
	return 0;
}