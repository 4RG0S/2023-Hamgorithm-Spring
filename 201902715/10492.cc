#include <iostream>
#include <string>

int N, M;
int arr[2000];
char dp[2000][2000];

bool solve(int s, int e) {
    if (s >= e) return true;

    if (dp[s][e] != -1) return dp[s][e];

    if (arr[s] != arr[e]) {
        dp[s][e] = 0;
        return false;
    }

    return dp[s][e] = solve(s + 1, e - 1);
}

int main() {
    std::string result = "";

    std::ios::sync_with_stdio(false);

    for (int i = 0; i < 2000; ++i) {
        for (int j = 0; j < 2000; ++j) {
            dp[i][j] = -1;
        }
    }

    int s, e;

    std::cin >> N;
    for (int i = 0; i < N; ++i) std::cin >> arr[i];
    std::cin >> M;
    for (int i = 0; i < M; ++i) {
        std::cin >> s >> e;
        --s;
        --e;

        if (solve(s, e)) result += "1\n";
        else result += "0\n";
    }

    std::cout << result << std::endl;

    return 0;
}