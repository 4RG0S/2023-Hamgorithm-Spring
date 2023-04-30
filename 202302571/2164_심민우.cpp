#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;

	vector<int> arry;
	for (int i = 0; i < n; i++)
		arry.push_back(i + 1);

	for (int i = 1; i < 2 * n - 3; i += 2)
		arry.push_back(arry[i]);
	cout << arry.back();

	return 0;
}