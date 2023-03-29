#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool desc(int a, int b) {
	return a > b;
}

int main() {
	int n;
	cin >> n;
	
	vector<int> arr;

	int ipt;
	for (int i = 0; i < n; i++) {
		cin >> ipt;
		arr.push_back(ipt);
	}

	sort(arr.begin(), arr.end(), desc);

	long sum = 0;
	for (int i = 0; i < n; i++) {
		if (arr[i] - i < 0)
			break;
		sum += arr[i] - i;
	}

	cout << sum;


	return 0;
}