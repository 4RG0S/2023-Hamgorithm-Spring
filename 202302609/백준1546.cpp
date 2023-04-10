#include <stdio.h>

int main(void) {
	double a = 0;
	int num = 0;
	double plus = 0;
	double score[1000] = { 0, };

	scanf_s("%d", &num);

	for (int i= 0;i<num;i++) {
		scanf_s("%lf", &score[i]);
	}

	a = score[0];
	for (int i =0;i<num;i++) {
		if (a< score[i]) {
			a = score[i];
		}
		else if(a>= score[i]) {
			a = a;
		}
	}

	for (int i = 0; i < num; i++) {
		plus = plus + (score[i] / a) * 100.0;
	}
	plus = plus / num;
	printf("%.2lf",plus);

	return 0;
}