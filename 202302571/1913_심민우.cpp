#include <iostream>
#include <string>

using namespace std;

int arry[1001][1001] = { {0,}, };

int main() {
	int n, num;
	cin >> n >> num;

	int i = 0, j = 0, count = n * n, k;

	for (k = 0; k <= n / 2; k++) {
		for (i = 0 + k; i < n - k; i++) {
			if (arry[i][j] == 0)
				arry[i][j] = count--;
		}
		i--;
		for (j = 0 + k; j < n - k; j++) {
			if (arry[i][j] == 0)
				arry[i][j] = count--;
		}
		j--;
		for (i = n - 1 - k; i >= 0 + k; i--) {
			if (arry[i][j] == 0)
				arry[i][j] = count--;
		}
		i++;
		for (j = n - 1 - k; j >= 0 + k; j--) {
			if (arry[i][j] == 0)
				arry[i][j] = count--;
		}
		j = k + 1;
	}

	string s;
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			cout << arry[i][j] << " ";
			if (arry[i][j] == num) {
				s = to_string(i + 1) + " " + to_string(j + 1);
			}
		}
		//if (i == n)
			//break;
		cout << "\n";
	}
	cout << s;

	return 0;
}