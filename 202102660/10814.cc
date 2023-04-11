#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

vector<pair<int, string>> v;

bool compare(pair<int, string> a, pair<int, string> b) {
    return a.first < b.first;
}

int main() {
    int n, a;
    string b;
    cin >> n;

    for (int i=0; i <n; i++) {
        cin >> a >> b;
        v.push_back(pair<int, string>(a, b));
    }
    stable_sort(v.begin(), v.end(), compare);

    for (int i=0; i <n; i++) {
        cout << v[i].first << " " << v[i].second << "\n";
    }

    return 0;
}