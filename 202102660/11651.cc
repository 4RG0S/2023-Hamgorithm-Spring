#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
    int N = 0;
    cin >> N;
    vector<pair<int, int>> v(N);

    for (int i = 0; i < N; i++) {
        cin >> v[i].second >> v[i].first;
    }

    sort(v.begin(), v.end());

    for (int i = 0; i < N; i++) {
        cout << v[i].second << " " << v[i].first << "\n";
    }
}