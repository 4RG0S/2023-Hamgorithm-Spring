#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    while (true) {
        string s;
        getline(cin, s);

        if (s[0] == '.')
            break;

        vector<int> sode;

        for (int i = 0; i < (int)s.size(); i++) {
            if (s[i] == '(')
                sode.push_back(1);
            else if (s[i] == ')') {
                if (!sode.empty() && sode.back() == 1)
                    sode.pop_back();
                else{
                    sode.push_back(-1);
                    break;
                }
            }
            else if (s[i] == '[')
                sode.push_back(2);
            else if (s[i] == ']') {
                if (!sode.empty() && sode.back() == 2)
                    sode.pop_back();
                else {
                    sode.push_back(-1);
                    break;
                }
            }
        }

        if (sode.empty())
            cout << "yes\n";
        else
            cout << "no\n";
    }

    return 0;
}