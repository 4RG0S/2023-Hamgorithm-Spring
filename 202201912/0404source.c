#include <stdio.h>

int main(void) 
{
	int a, b, c, result = -1;
	scanf("%d%d%d", &a, &b, &c);
	if (b < c) {
		result = a / (c - b) + 1;
	}
	printf("%d", result);

	return 0;
}