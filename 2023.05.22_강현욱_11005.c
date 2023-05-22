#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main()
{
	int x, y = 0;
	scanf("%d %d", &x, &y);
	int na = 0;
	char jin[1000] = { 0 };
	int i = 0;

	while (1)
	{
		na = x % y;

		if (na > 9)
		{
			jin[i] = (char)(na + 55);
		}
		else
		{
			jin[i] = (char)(na + 48);
		}

		x = x / y;

		if (x == 0)
		{
			break;
		}

		i++;
	}

	int s = 0;

	for (s = i; s >= 0; s--)
	{
		printf("%c", jin[s]);
	}

	return 0;
}