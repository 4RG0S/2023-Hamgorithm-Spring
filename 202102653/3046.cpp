#include <iostream>

int main(void) {
    // Sync off
    std::ios_base::sync_with_stdio(false);

    // Declare variable;
    int num1, num2, avg;
    
    // Input
    std::cin >> num1 >> avg;

    num2 = avg * 2 - num1;

    // Output
    std::cout << num2 << std::endl;

    return 0;
}