#include<stdio.h>

int ary[10];
int visit[10];
int m, n;
void sequence(int level)
{
	int i;
	if (level == n)
	{
		for (i = 0; i < n; i++)
		{
			printf("%d ", ary[i]);
		}
		printf("\n");

		return;
	}

	for (i = 1; i <= m; i++)
	{
		if (visit[i] == 0)
		{
			visit[i] = 1;
			ary[level] = i;
			sequence(level + 1);

			visit[i] = 0;
		}
	}
}

int main(void)
{
	scanf("%d %d", &m, &n);

	sequence(0);

	return 0;
}