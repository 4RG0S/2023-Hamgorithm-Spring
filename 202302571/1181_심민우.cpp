#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

bool comp(string a, string b) {
	if (a.length() == b.length())
		return a < b;
	else
		return a.length() < b.length();
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;
	cin.ignore();

	vector<string> str;
	string tmp;
	for (int i = 0; i < n; i++) {
		getline(cin, tmp);
		str.push_back(tmp);
	}
	sort(str.begin(), str.end(), comp);
	cout << str[0] << "\n";
	for (int i = 1; i < n; i++) {
		if (str[i] == str[i - 1])
			continue;
		else
			cout << str[i] << "\n";
	}

	return 0;
}