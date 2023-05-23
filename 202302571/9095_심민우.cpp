#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int dp[11];

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    while (t--) {
        int n;
        cin >> n;

        if (dp[n] == 0) {
            for (int i = 4; i <= n; i++)
                dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
        }
        cout << dp[n] << '\n';
    }

    return 0;
}