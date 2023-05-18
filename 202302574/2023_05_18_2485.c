#include<stdio.h>
int GCD(int a, int b) {
	if (b == 0) return a;
	return GCD(b, a % b);
}
int main() {
	int num, a, temp = 0, gcd=0, sum=0;
	int arr[100000] = { 0, };
	scanf("%d", &num);
	scanf("%d", &temp);
	for (int i = 0; i < num-1; i++) {
		scanf("%d", &a);
		arr[i] = a - temp;
		temp = a;
	}
	gcd = arr[0];
	for (int i = 1; i < num - 1; i++) {
		gcd = GCD(arr[i], gcd);
	}
	for (int i = 0; i < num - 1; i++) {
		sum += arr[i] / gcd - 1;
	}
	printf("%d", sum);
}