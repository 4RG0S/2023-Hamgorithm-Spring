#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;
    vector<vector<int>> chess(n, vector<int>(m, 0));

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < m; j++) {
            if (s[j] == 'W')
                chess[i][j] = 0;//w=0
            else
                chess[i][j] = 1;//b=1
        }
    }

    int w = 0, b = 0;
    int Min = 999;
    for (int i = 0; i <= n - 8; i++) {
        for (int j = 0; j <= m - 8; j++) {
            w = 0, b = 0;
            for (int k = 0; k < 8; k++) { // wbwb... bwbw...
                for (int l = 0; l < 8; l++) {
                    if (k % 2 == 0) {
                        if (l % 2 == 0) {
                            if (chess[k + i][l + j] == 1)
                                w++;
                            else
                                b++;
                        }
                        else {
                            if (chess[k + i][l + j] == 0)
                                w++;
                            else
                                b++;
                        }

                    }
                    else {
                        if (l % 2 == 0) {
                            if (chess[k + i][l + j] == 0)
                                w++;
                            else b++;
                        }
                        else {
                            if (chess[k + i][l + j] == 1)
                                w++;
                            else b++;
                        }
                    }
                }
            }
            Min = min(Min, min(w, b));
        }
    }

    cout << Min;

    return 0;
}