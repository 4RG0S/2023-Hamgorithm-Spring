#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n, k;
	cin >> k >> n;

	vector<unsigned long> lanport;

	unsigned long max = 0, tmp;
	for (int i = 0; i < k; i++) {
		cin >> tmp;
		lanport.push_back(tmp);
		if (tmp > max)
			max = tmp;
	}

	unsigned long left = 1, right = max, mid, sum;
	tmp = 0;

	while (left <= right) {
		mid = (left + right) / 2;
		sum = 0;
		for (int i = 0; i < k; i++)
			sum += lanport[i] / mid;

		if (sum >= n) {
			left = mid + 1;
			if (mid >= tmp)
				tmp = mid;
		}
		else
			right = mid - 1;
	}
	cout << tmp << "\n";

	return 0;
}