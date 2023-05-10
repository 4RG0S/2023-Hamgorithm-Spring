#include <iostream>
#include <vector>
#include <algorithm>

std::vector<std::pair<int, int>> coord;

int main() {
    int N;
    int x, y;
    std::scanf("%d", &N);

    for(int i = 0; i < N; i++) {
        std::scanf("%d %d", &x, &y);
        coord.push_back({x, y});
    }
    sort(coord.begin(), coord.end());
    for(int i = 0; i < N; i++) {
        std::printf("%d" " %d\n", coord[i].first, coord[i].second);
    }
}
