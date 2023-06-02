#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int pos_intnum[4001];
int neg_intnum[4001];

bool comppair(pair<int, int> a, pair<int, int> b) {
    if (a.first == b.first)
        return a.second < b.second;
    else
        return a.first > b.first;
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> a(n);
    int sum = 0;
    int maxa = -4001, mina = 4001;

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        sum += a[i];
        maxa = max(a[i], maxa);
        mina = min(a[i], mina);
        if (a[i] >= 0)
            pos_intnum[a[i]]++;
        else
            neg_intnum[-a[i]]++;
    }

    if (round((double)sum / n) == -0)
        cout << 0 << '\n';
    else
        cout << round((double)sum / n) << '\n';

    sort(a.begin(), a.end());
    cout << a[n / 2] << '\n';

    int maxi = 0;
    vector<pair<int, int>> b;
    pair<int, int> t;
    t.first = pos_intnum[0];
    t.second = 0;
    b.push_back(t);

    for (int i = 1; i <= 4000; i++) {
        if (pos_intnum[i] > 0) {
            t.first = pos_intnum[i];
            t.second = i;
            b.push_back(t);
        }
        if (neg_intnum[i] > 0) {
            t.first = neg_intnum[i];
            t.second = -i;
            b.push_back(t);
        }
    }
    
    sort(b.begin(), b.end(), comppair);
    if (b.size() < 2)
        cout << b[0].second << '\n';
    else if (b[0].first == b[1].first)
        cout << b[1].second << '\n';
    else
        cout << b[0].second << '\n';

    cout << maxa - mina;
    
    return 0;
}