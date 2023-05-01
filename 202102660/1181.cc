#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> v;

bool compare(string a, string b) {
    if (a.length() == b.length()) {
        return a.compare(b) < 0;
    } else return a.length() < b.length();
}

int main() {
    int n;
    string a;
    cin >> n;

    for (int i=0; i<n; i++) {
        cin >> a;
        v.push_back(a);
    }
    sort(v.begin(), v.end(), compare);

    v.erase(unique(v.begin(), v.end()), v.end());
    for (string s : v) {
        cout << s << "\n";
    }
    return 0;
}