#include <iostream>
using namespace std;

#define ARRY 10000001

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;

	int pos_int[ARRY] = { 0, };
	int neg_int[ARRY] = { 0, };
	int zero = 0;

	int input;
	for (int i = 0; i < n; i++) {
		cin >> input;
		if (input > 0)
			pos_int[input]++;
		else if (input < 0)
			neg_int[-input]++;
		else
			zero++;
	}

	int m;
	cin >> m;

	for (int i = 0; i < m; i++) {
		cin >> input;
		if (input > 0)
			cout << pos_int[input] << " ";
		else if (input < 0)
			cout << neg_int[-input] << " ";
		else
			cout << zero << " ";
	}

	return 0;
}