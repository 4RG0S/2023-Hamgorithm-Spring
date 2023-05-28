#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);


    string s;
    cin >> s;

    vector<bool> stick;

    int n = (int)s.size();
    int sum = 0;

    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            if (s[i + 1] == ')') {
                for (int j = 0; j < stick.size(); j++)
                    sum++;
            }
            else
                stick.push_back(true);
        }
        else if (s[i] == ')' && s[i - 1] != '(') {
            stick.pop_back();
            sum++;
        }
    }

    cout << sum;

    return 0;
}