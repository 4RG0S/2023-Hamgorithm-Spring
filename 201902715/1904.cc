#include <iostream>

int main() {
    int N;
    std::cin >> N;

    int *solution = (int *)malloc((N + 1) * sizeof(int));
    solution[0] = 0;
    solution[1] = 1;
    solution[2] = 2;
    for (int i = 3; i <= N; ++i) {
        solution[i] = solution[i - 1] + solution[i - 2];
        solution[i] %= 15746;
    }
    std::cout << solution[N];

    return 0;
}
