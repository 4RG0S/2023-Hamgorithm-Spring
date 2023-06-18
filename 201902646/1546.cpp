#include <iostream>
#include <algorithm>

int main() {

	int N;	
	double sum = 0;
	std::cin >> N;
	double arr[1001];

	for(int i = 0; i < N; i++) {
		std::cin >> arr[i];
	}
	std::sort(arr, arr + N);	
	for(int i = 0; i < N; i++) {
		sum = sum + (arr[i] / arr[N - 1]) * 100;
	}
 
	std::cout << sum / N << std::endl;
	return 0;
}
