#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int sum[100001] = { 0, };

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    cin >> sum[0];
    for (int i = 1; i < n; i++) {
        cin >> sum[i];
        sum[i] += sum[i - 1];
    }

    for (int i = 0; i < m; i++) {
        int k, l;
        cin >> k >> l;

        if (k - 2 < 0)
            cout << sum[l - 1] - 0 << '\n';
        else
            cout << sum[l - 1] - sum[k - 2] << '\n';
    }

    return 0;
}