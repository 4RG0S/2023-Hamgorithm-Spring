#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;

	vector<int> arry;
	int tmp;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		arry.push_back(tmp);
	}
	sort(arry.begin(), arry.end());
	for (int i = 0; i < n; i++) {
		cout << arry[i] << "\n";
	}


	return 0;
}