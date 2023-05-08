#include <stdio.h>

int main() {
	char input[10];
	int size = 10;
	int i = 0;

	scanf("%s", input);

	for (i = 0; i < 10; i++) {
		if (input[i] < '0' || input[i] > '9') {
			break;
		}
	}

	size = i;

	for (i = 0; i < size; i++) {
		if (input[i] > '1')
			break;
		else if (input[i] == '0' && size != 1) {
			size--;
			break;
		}
	}

	printf("%d\n", size);
	return 0;
}