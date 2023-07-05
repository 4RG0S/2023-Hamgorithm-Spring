#include <iostream>

#define MIN(a, b) (a) < (b) ? (a) : (b)

int solution[100001];

int main() {
    int N;

    std::cin >> N;

    for (int i = 1; i <= N; i++) {
        int j = 1;

        solution[i] = i;

        while (j * j <= i) {
            solution[i] = MIN(solution[i], solution[i - j * j] + 1);
            j++;
        }
    }

    std::cout << solution[N];

    return 0;
}