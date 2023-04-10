#include <stdio.h>

int main(void) {
	int num[9] = { 0, };
	int a = 0;
	int b = 0;

	for (int i =0; i<9;i++) {
		scanf_s("%d",&num[i]);

	}
	a = num[0];
	for (int i=0; i<9;i++) {
		if (a < num[i]) {
			a = num[i];
		}
		else if (a >= num[i]) {
			a = a;
		}
	}
	
	for (int i =0; i<9;i++) {
		if (num[i]==a) {
			b = i + 1;
			break;
		}
	}

	printf("%d\n%d", a,b);
	return 0;
}