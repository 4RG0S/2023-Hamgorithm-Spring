#include <stdio.h>

int main(void) {
	while (1) {


		int a[4] = { 0, };
		int num = 0;
		int len = 0;
		int size = 0;

		scanf_s("%d", &num);

		if (num == 0) {
			return 0;
			break;
		}
		for (int i = 0; i <= 3; i++) {
			a[i] = num % 10;
			num /= 10;
			if (num == 0) {
				len = i + 1;
				break;
			}
		}
		for (int i = 0; i <= 3; i++) {
			if (a[i] == 1) {
				size += 2;
			}
			else if (a[i] == 0) {
				size += 4;
			}
			else {
				size += 3;
			}
			if (len - 1 == i) {
				break;
			}
		}
		size = size + len + 1;
		printf("%d\n", size);
	}
	return 0;
}