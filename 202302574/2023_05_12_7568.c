#include<stdio.h>
int main() {
	int arr[100] = { 0, };
	int i, j, num;
	scanf("%d", &num);
	for (i = 0; i < num; i++) {
		scanf("%d", &arr[2 * i]);
		scanf("%d", &arr[2 * i + 1]);
	}
	for (i = 0; i < num; i++) {
		int count = 1;
		for (j = 0; j < num; j++) {
			count = count + (arr[2 * i] < arr[2 * j] && arr[2 * i + 1] < arr[2 * j + 1]);
		}
		printf("%d ", count);
	}
}