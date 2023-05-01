#include <stdio.h>

int main(void) 
{
	int max = 0, num[9], index;
	for (int i = 0; i < 9; i++) {
		scanf("%d", &num[i]);
		if (max < num[i]) {
			max = num[i];
			index = i;
		}
	}
	printf("%d\n", max;
	printf("%d",index + 1);

	return 0;
}