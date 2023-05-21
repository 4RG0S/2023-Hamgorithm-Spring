#include <stdio.h>
#include <string.h>

int main(void) {
	int count;
	char str[102];
	char stack[102];

	while (1) {
		count = 0;
		memset(stack, 0, 102);

		fgets(str, 102, stdin);
		if (str[0] == '.') break;
		for (int i = 0; str[i] != '.'; i++) {
			if (str[i] == '(') {
				stack[count++] = '(';
			}

			else if (str[i] == '[') {
				stack[count++] = '[';
			}

			else if (str[i] == ')') {
				if (stack[count - 1] == '(') count--;
				else stack[count++] = ')';
			}

			else if (str[i] == ']') {
				if (stack[count - 1] == '[') count--;
				else stack[count++] = ']';
			}
		}

		if (!count) puts("yes");
		else puts("no");
	}

	return 0;
}
