#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>

// global variables
size_t numberOfDigits;
size_t digitArr[500001];
size_t temp[500001];
unsigned long long result = 0;

// Function merge
void merge(size_t left, size_t right) {
	size_t mid = (left + right) / 2;
	size_t L = left;
	size_t R = mid + 1;
	size_t k = left;
	size_t count = 0;

	while (L <= mid && R <= right) {
		if (digitArr[L] <= digitArr[R]) {
			temp[k++] = digitArr[L++];
			result += (unsigned long long)count;
		} else {
			temp[k++] = digitArr[R++];
			count++;
		}
	}

	if (L > mid) {
		size_t s = R;
		while (s <= right) {
			temp[k++] = digitArr[s++];
			count++;
		}
	} else {
		size_t s = L;
		while (s <= mid) {
			temp[k++] = digitArr[s++];
			result += (unsigned long long)count;
		}
	}

	for (size_t t = left; t <= right; t++) {
        digitArr[t] = temp[t];
    }
}

// Function mergeSort
void mergeSort(size_t left, size_t right) {
	if (left < right) {
		size_t mid = (left + right) / 2;
		mergeSort(left, mid);
		mergeSort(mid + 1, right);
		merge(left, right);
	}
}

int main() {
    // Sync off
    std::ios_base::sync_with_stdio(false);

    // Input
	std::cin >> numberOfDigits;
	for (size_t i = 0; i < numberOfDigits; i++) {
		size_t num;
		std::cin >> num;
		digitArr[i] = num;
	}

    // Sort & Calculate result
	mergeSort(0, numberOfDigits - 1);

    // Output result
	std::cout << result << std::endl;

    return 0;
}
