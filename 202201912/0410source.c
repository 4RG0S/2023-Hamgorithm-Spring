#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
void quickSort(int data[], int l, int r) {
	int left = l;
	int right = r;
	int pivot = data[(l + r) / 2];

	while (left <= right) {
		while (data[left] < pivot) left++;
		while (data[right] > pivot) right--;
		if (left <= right) {

			int temp = data[left];
			data[left] = data[right];
			data[right] = temp;
			left++;
			right--;
		}
	}
	if (l < right) {
		quickSort(data, l, right);
	}
	if (r > left) {
		quickSort(data, left, r);
	}
}
int main() {

	int n, l;
	int i;
	int aa[1000] = { 0 };
	scanf("%d %d", &n, &l);

	for (i = 0; i < n; i++) {
		scanf("%d", &aa[i]);
	}
	quickSort(aa, 0, n - 1);

	for (i = 0; i < n; i++) {
		if (l >= aa[i])
		{
			l += 1;
		}
		else
			break;
	}
	printf("%d", l);
	return 0;
}