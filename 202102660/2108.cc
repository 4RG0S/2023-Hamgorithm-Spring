#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

bool cmp(pair<int, int>& a, pair<int, int>& b) {
    if (a.second == b.second) {
        return a.first < b.first;
    }
    return a.second > b.second;
}

int main() {
    int n, m=0, mid, freq, l, idx=0;
    cin >> n;
    vector<int> vec(n);

    for (int i = 0; i < n; i++) {
        cin >> vec[i];
        m += vec[i];
    }

    vector<int> b(8001, 0);
    m = round(float(m)/n);
    sort(vec.begin(), vec.end());
    mid = vec[n/2];
    l = vec[n-1] - vec[0];
    for (int i : vec) {
        b[i+4000]++;
    }

    bool is_second = false;
    int max_freq = *max_element(b.begin(), b.end());
    for (int i=0; i < 8001; i++) {
        if (b[i]==max_freq) {
            if (is_second) {
                freq = i-4000;
                break;
            } else {
                freq = i-4000;
                is_second = true;
            }
        }
    }
    cout << m << '\n' << mid << '\n' << freq << '\n' << l << '\n';
    return 0;
}