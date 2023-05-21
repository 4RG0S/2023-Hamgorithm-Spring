#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int ground[501][501];

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, b;
    cin >> n >> m >> b;

    int min = 257, max = -1;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> ground[i][j];
            if (ground[i][j] < min)
                min = ground[i][j];
            if (ground[i][j] > max)
                max = ground[i][j];
        }
    }

    int min_hour = 2147483647;
    int floor = min;
    for (int k = min; k <= max; k++) {
        int put = 0, del = 0, bag = b;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (k - ground[i][j] < 0) {
                    del += ground[i][j] - k;
                    bag += ground[i][j] - k;
                }
                if (k - ground[i][j] > 0)
                    put += k - ground[i][j];
            }
        }
        if (put > bag)
            continue;
        int workhour = (del * 2) + put;
        if (workhour <= min_hour) {
            min_hour = workhour;
            floor = k;
        }
    }

    cout << min_hour<< " "<< floor;

    return 0;
}