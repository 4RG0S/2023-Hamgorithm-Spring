#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;

	int giho_N[50];
	cin >> giho_N[0];
	int max_arry = 0, max = giho_N[0];
	int count = 0;

	for (int i = 1; i < N; i++) {
		cin >> giho_N[i];
		if (giho_N[i] > max) {
			max_arry = i;
			max = giho_N[i];
		}
	}
	while (max != giho_N[0]) {
		giho_N[0]++;
		giho_N[max_arry]--;
		max = giho_N[0];
		count++;

		for (int i = 1; i < N; i++) {
			if (giho_N[i] > max) {
				max_arry = i;
				max = giho_N[i];
			}
		}
	}

	for (int i = 1; i < N; i++) {
		if (giho_N[0] == giho_N[i]) {
			count++;
			break;
		}
	}

	cout << count << endl;

	return 0;
}