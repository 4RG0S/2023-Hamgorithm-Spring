#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main()
{
	int N;
	int list[100] = { 0 };
	int myscore;
	int P;

	int rankcount = 0;
	int myrank = 1;

	scanf("%d %d %d", &N, &myscore, &P);
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &list[i]);
	}

	for (int i = 0; i < N; i++)
	{
		if (myscore < list[i])
		{
			myrank++;
		}
		else if (myscore == list[i])
		{

		}
		else
		{
			break;
		}
		rankcount++;
	}

	if (rankcount == P)
	{
		myrank = -1;
	}
	if (N == 0)
	{
		myrank = 1;
	}

	printf("%d\n", myrank);
	return 0;
}