#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable:6031)
#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int a, b, n;
	int result;		

	scanf("%d %d %d", &a, &b, &n);	

	for (int i = 0; i < n; i++)		
	{
		a = (a % b)*10;		
		result = a / b;	
	}

	printf("%d", result);

	return 0;
}