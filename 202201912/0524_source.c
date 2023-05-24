#include <stdio.h>
int main(void)
{
	int N;
	char R[105][105];
	int r_cnt = 0;
	int c_cnt = 0;

	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		scanf("%s", R[i]);
		int cur = 0;
		for (int k = 0; k < N; k++)
		{
			if (R[i][k] == '.') cur++;
			else
			{
				if (cur >= 2) r_cnt++;
				cur = 0;
			}
		}
		if (cur >= 2) r_cnt++;
	}

	for (int i = 0; i < N; i++)
	{
		int cur = 0;
		for (int j = 0; j < N; j++)
		{
			if (R[j][i] == '.') cur++;
			else
			{
				if (cur >= 2) c_cnt++;
				cur = 0;
			}
		}
		if (cur >= 2) c_cnt++;
	}

	printf("%d %d", r_cnt, c_cnt);
	return 0;
}