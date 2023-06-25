#include <iostream>

int main(void) {
    // Sync off
    std::ios_base::sync_with_stdio(false);

    // Declare variables
    ssize_t numberOfLine;

    // Input
    std::cin >> numberOfLine;

    // Output
    for(ssize_t i = 0; i < numberOfLine; i++) {
        for(ssize_t j = numberOfLine; j > i; j--) {
            std::cout << '*';
        }
        std::cout << '\n';
    }

    return 0;
}
