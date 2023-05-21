#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    vector<int> min(n);

    for (int i = 0; i < n; i++)
        cin >> min[i];
    sort(min.begin(), min.end());

    int sum = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++)
            sum += min[j];
    }

    cout << sum;

    return 0;
}