#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long n, m;
    cin >> n >> m;

    vector<long> tree(n);
    for (long i = 0; i < n; i++)
        cin >> tree[i];
    sort(tree.begin(), tree.end());

    long left = 0, right = tree[n - 1], mid = 0, max = 0;

    while (left <= right) { //left > right break;
        mid = (left + right) / 2;
        long sum = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (tree[i] - mid <= 0)
                break;
            sum += tree[i] - mid;
        }
        if (sum >= m) {
            left = mid + 1;
            if (mid >= max)
                max = mid;
        }
        else
            right = mid - 1;
    }
    cout << max;

    return 0;
}