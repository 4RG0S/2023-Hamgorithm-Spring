#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<string.h>

int main(void)
{
	int min6 = 1000;
	int min1 = 1000;
	int N, M;
	int price = 0;
	scanf("%d %d", &N, &M);
	for (int i = 0; i < M; i++)
	{
		int temp6, temp1;
		scanf("%d %d", &temp6, &temp1);
		if (temp6 < min6)
		{
			min6 = temp6;
		}
		if (temp1 < min1)
		{
			min1 = temp1;
		}
	}
	if (min1 * 6 < min6)
	{
		price += min1 * N;
	}
	else if (min6 < min1 * (N % 6))
	{
		if (N % 6 == 0)
		{
			price += min6 * (N / 6);
		}
		else
		{
			price += min6 * (N / 6) + min6;
		}
	}
	else
	{
		price += (N / 6) * min6;
		N %= 6;
		price += N * min1;
	}
	printf("%d\n", price);


	return 0;
}
