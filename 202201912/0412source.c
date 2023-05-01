#include <stdio.h>

#define POW3(X) (X*X*X)

int main()
{
	for (int i = 2; i <= 100; i++)
	{
		int x[101] = { 0, };
		for (int a = 2; a < i; a++)
			for (int b = a; b < i; b++)
				for (int c = b; c < i; c++)
					if (POW3(i) == POW3(a) + POW3(b) + POW3(c) && !(x[a] && x[b] && x[c]))
					{
						printf("Cube = %d, Triple = (%d,%d,%d)\n", i, a, b, c);
						x[a] = x[b] = x[c] = 1;
					}
	}
	return 0;
}