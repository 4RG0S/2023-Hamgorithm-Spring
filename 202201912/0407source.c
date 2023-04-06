#include <stdio.h>
int main(void)
{
	int t, a, b, c;
	scanf("%d", &t);
	if (t % 10 == 0)
	{
		a = t / 300;
		t %= 300;
		b = t / 60;
		t %= 60;
		c = t / 10;
		printf("%d %d %d", a, b, c);
	}

	else
		printf("-1");
}