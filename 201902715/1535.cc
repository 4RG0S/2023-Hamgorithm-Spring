#include <array>
#include <iostream>

#define MAX(a, b) (a > b) ? (a) : (b)

int main() {
    int N;
    std::array<int, 20> cost;
    std::array<int, 20> happy;
    std::array<std::array<int, 101>, 20> solution;

    std::cin >> N;

    for (int i = 0; i < N; i++) {
        std::cin >> cost[i];
    }
    for (int i = 0; i < N; i++) {
        std::cin >> happy[i];
    }

    solution[0][0] = 0;
    for (int w = 0; w <= 100; w++) {
        if (w > cost[0])
            solution[0][w] = happy[0];
        else
            solution[0][w] = 0;
    }

    for (int i = 1; i < N; i++) {
        for (int w = 0; w <= 100; w++) {
            solution[i][w] = solution[i - 1][w];

            if (w > cost[i]) {
                solution[i][w] = MAX(solution[i][w],
                                     solution[i - 1][w - cost[i]] + happy[i]);
            }
        }
    }

    std::cout << solution[N - 1][100];

    return 0;
}