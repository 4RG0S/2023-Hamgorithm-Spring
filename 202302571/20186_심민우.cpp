#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end(), greater<int>());

    int sum = 0;
    for (int i = 0; i < k; i++)
        sum += a[i] - i;

    cout << sum;
    
    return 0;
}