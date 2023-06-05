#include <stdio.h>

int aa[2000001];
int main(void)
{
	int num;
	int i;
	int k;
	scanf("%d", &num);
	for (i = 1; i <= num; i++) {
		scanf("%d", &k);
		++aa[k + 1000000];
	}
	for (i = 0; i <= 2000000; i++) {
		while (aa[i] > 0) {
			printf("%d\n", i - 1000000);
			aa[i]--;
		}
	}
	return 0;
}