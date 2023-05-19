#include <iostream>

int main() {
    int N;
    int dp[5001];
    dp[3] = dp[5] = 1;
    dp[0] = dp[1] = dp[2] = dp[4] = -1;

    std::cin >> N;

    for(int i = 6; i <=N; i++) {
        int count = dp[i-1]+1;
        if(dp[i-3]==-1 && dp[i-5]==-1) {
            dp[i] = -1;
        }
        else if (dp[i-3]!=-1 && dp[i-5]==-1) {
            dp[i] = dp[i-3] + 1;
        }
        else if (dp[i-3]==-1 && dp[i-5]!=-1) {
            dp[i] = dp[i-5] + 1;
        }
        else  {
            dp[i] = std::min(dp[i-3]+1, dp[i-5]+1);
        }
    }
    std::cout<< dp[N] << std::endl;
    return 0;
}
