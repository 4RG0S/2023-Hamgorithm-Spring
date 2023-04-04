#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
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

	int m;
	cin >> m;
	for (int i = 0; i < m; i++) {
		int left = 0;
		int right = n - 1;
		int mid;
		cin >> tmp;
		bool check = false;
		while (left <= right) {//left > right break;
			mid = (left + right) / 2;
			if (arry[mid] > tmp)
				right = mid - 1;
			else if (arry[mid] < tmp)
				left = mid + 1;
			else if (arry[mid] == tmp) {
				check = true;
				break;
			}
		}
		if (check == true) 
			cout << "1\n";
		else
			cout << "0\n";
	}

	return 0;
}