#include<stdio.h>
int main() {
	/*1 => 0
	* 0 => 1
	* ´İÈû = 0, ¿­¸² = 1
	*
	int N=15;
	int arr[100] = {0,};
	for (int i = 1; i <= N; i++) {
		for (int j = i; j <= N; j += i) {
			arr[j] = (arr[j] + 1) % 2;
		}
	}
	for (int i = 1; i <= N; i++) {
		printf("%d", arr[i]);
	}
	*/
	int N, count = 0;
	scanf("%d", &N);
	for (int i = 1; i * i <= N; i++) {
		count++;
	}
	printf("%d", count);

}