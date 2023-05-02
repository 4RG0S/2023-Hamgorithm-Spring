#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable:6031)
#pragma warning(disable:4996)
#include <stdio.h>

int main(void)
{
	int A = 0, B = 0, C = 0;
	scanf("%d %d %d", &A, &B, &C);
	int hour = A;
	int minute = B + C;
	while (minute > 59)
	{
		minute = minute - 60;
		hour++;
	}
	while (hour > 23)
		hour = hour - 24;
	printf("%d %d", hour, minute);
	return 0;
}