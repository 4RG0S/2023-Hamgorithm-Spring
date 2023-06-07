#include<stdio.h>
int main() {
	int a, b, c;
	scanf("%d%d%d", &a, &b, &c);

	if (a > b) {
		int temp = b;
		b = a;
		a = temp;
	}
	if (b > c) {
		int temp = c;
		c = b;
		b = temp;
	}
	if (a > b) {
		int temp = b;
		b = a;
		a = temp;
	}

	printf("%d", b);
}