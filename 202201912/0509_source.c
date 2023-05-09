#include <stdio.h>
#include <stdlib.h>

#define MAX	100000

int ary[MAX];

int compare(void* first, void* second)
{
	if (*(int*)first > *(int*)second)
		return 1;
	else if (*(int*)first < *(int*)second)
		return -1;
	else
		return 0;
}

int main()
{
	int num;
	int X;
	int i;
	int start, end;
	int cnt;

	scanf("%d", &num);
	for (i = 0; i < num; i++)
		scanf("%d", &ary[i]);
	scanf("%d", &X);

	qsort(ary, num, sizeof(int), compare);

	start = 0;
	end = num - 1;
	cnt = 0;

	while (start < end)
	{
		if (ary[start] + ary[end] == X)
		{
			cnt++;
			start++;
			end--;
		}
		else if (ary[start] + ary[end] < X)
		{
			start++;
		}
		else
		{
			end--;
		}
	}

	printf("%d", cnt);
}