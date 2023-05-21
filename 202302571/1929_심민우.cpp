#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

bool prime[10000001];

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long m, n;
    cin >> m >> n;

    prime[1] = true;

    for (long i = 2; i <= n; i++) {
        if (!prime[i]) {
            for (long j = i * 2; j <= n; j += i)
                prime[j] = true;
        }
    }

    for (long i = m; i <= n; i++) {
        if (!prime[i])
            cout << i << "\n";
    }

    return 0;
}