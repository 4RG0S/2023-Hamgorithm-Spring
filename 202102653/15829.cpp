#include <iostream>
#include <vector>

int main(void) {
    // Sync off
    std::ios_base::sync_with_stdio(false);

    // Declare variables
    unsigned int lengthOfString;
    std::vector <char> charVec;
    char ch;
    long long sum = 0, MOD = 1234567891, R = 1;

    // Input
    std::cin >> lengthOfString;

    for(unsigned int i = 0; i < lengthOfString; i++) {
        std::cin >> ch;
        charVec.push_back(ch);
    }

    for(char ch : charVec) {
        sum = (sum + (ch - 'a' + 1) * R) % MOD;
        R = (R * 31) % MOD;
    }

    // Output
    std::cout << sum << std::endl;

    return 0;
}