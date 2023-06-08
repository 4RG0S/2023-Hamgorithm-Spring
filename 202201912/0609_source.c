#include <stdio.h>
#include <math.h>


int main(void)
{
	float x1, x2, y1, y2, cx, cy, r;
	int n, i, j, t;
	int count = 0;
	scanf("%d", &t);
	for (i = 0; i < t; i++)
	{
		scanf("%f %f %f %f", &x1, &y1, &x2, &y2);
		scanf("%d", &n);
		for (j = 0; j < n; j++)
		{
			scanf("%f %f %f", &cx, &cy, &r);
			float d1 = sqrt(pow((x1 - cx), 2) + pow((y1 - cy), 2));
			float d2 = sqrt(pow((x2 - cx), 2) + pow((y2 - cy), 2));
			if (d1 < r && d2 > r)
			{
				count = count + 1;
			}
			else if (d1 > r && d2 < r)
			{
				count = count + 1;
			}
		}
		printf("%d\n", count);
		count = 0;
	}
	return 0;
}