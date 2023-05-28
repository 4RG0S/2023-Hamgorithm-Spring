#include <stdio.h>
#include <string.h>
#include <math.h>

char board[101][101];
char buf[100000];
int idx;

int main(int argc, char** argv)
{
	int i, j, n;
	int len;
	scanf("%d%*c", &n);

	while (n--)
	{
		idx = 0;
		gets(buf);

		len = (int)sqrt(strlen(buf));

		for (i = 0; i < len; i++)
		{
			for (j = 0; j < len; j++)
			{
				board[i][j] = buf[i * len + j];
			}
		}
		idx = 0;
		for (j = len - 1; j >= 0; j--)
		{
			for (i = 0; i < len; i++)
			{
				buf[idx++] = board[i][j];
			}
		}
		buf[idx] = '\0';
		puts(buf);

	}
	return 0;
}