#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> play(n);
    unsigned long max = 0, sum = 0;

    for (int i = 0; i < n; i++) {
        cin >> play[i];
        if (play[i] > max)
            max = play[i];
        sum += play[i];
    }
    sum -= max;

    if (sum >= max)
        cout << sum + max;
    else
        cout << (2 * sum) + 1;

    return 0;
}
