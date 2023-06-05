#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool comp_t(pair<int, int> a, pair<int, int> b) {
    if (a.second == b.second)
        return a.first < b.first;
    return a.second < b.second;
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<pair<int, int>> booking(n);
    for (int i = 0; i < n; i++) {
        cin >> booking[i].first >> booking[i].second;
    }
    sort(booking.begin(), booking.end(), comp_t);

    int sum = 1;
    int last = booking[0].second;
    for (int i = 1; i < n; i++) {
        if (last <= booking[i].first) {
            sum++;
            last = booking[i].second;
        }
    }
    cout << sum;

    return 0;
}