#include<stdio.h>
int e, s, m, year;
int main(void)
{
	scanf("%d %d %d", &e, &s, &m);

	while (1)
	{
		if (e == s && s == m && m == 1)
			break;
		year++;
		e--;
		s--;
		m--;
		if (e < 1)
			e = 15;
		if (s < 1)
			s = 28;
		if (m < 1)
			m = 19;
	}

	printf("%d\n", ++year);
	return 0;
}