#include <stdio.h>

int a[1000001];

int main(void)
{
	int num;
	scanf("%d", &num);

	a[1] = 0;

	int i;
	for (i = 2; i <= num; i++)
	{
		a[i] = a[i - 1] + 1;

		if (i % 2 == 0 && a[i] > a[i / 2] + 1)
		{
			a[i] = a[i / 2] + 1;
		}

		if (i % 3 == 0 && a[i] > a[i / 3] + 1)
		{
			a[i] = a[i / 3] + 1;
		}
	}
	printf("%d", a[num]);
	return 0;
}