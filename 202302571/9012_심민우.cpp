#include <iostream>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int t;
	cin >> t;
	cin.ignore();
	string str;
	for (int i = 0; i < t; i++) {
		getline(cin, str);
		int open = 0, close = 0;
		for (int j = 0; j < str.length(); j++) {
			if (open <= close && str[j] == ')') {
				close = -1;
				break;
			}
			if (str[j] == '(')
				open++;
			else if (str[j] == ')')
				close++;
		}
		if (open == close)
			cout << "YES\n";
		else
			cout << "NO\n";
	}

	return 0;
}