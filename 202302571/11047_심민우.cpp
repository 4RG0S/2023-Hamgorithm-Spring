#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n, k;
	cin >> n >> k;

	vector<int> coin;
	for (int i = 0; i < n; i++) {
		int tmp;
		cin >> tmp;
		coin.push_back(tmp);
	}
	int needcoin = 0;
	for (int i = n - 1; i >= 0; i--) {
		if (coin[i] > k)
			continue;
		needcoin += k / coin[i];
		k -= coin[i] * (k / coin[i]);
		if (k == 0)
			break;
	}

	cout << needcoin;

	return 0;
}