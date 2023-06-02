#include <iostream>
#include <stack>

int main(void) {
    // Sync off
    std::ios_base::sync_with_stdio(false);

    // Declare variables
    ssize_t numberOfNumbers;
    ssize_t number, sum = 0;
    std::stack <ssize_t> numberStack;

    // Input
    std::cin >> numberOfNumbers;

    for(ssize_t i = 0; i < numberOfNumbers; i++) {
        std::cin >> number;
        if(number == 0) {
            if(numberStack.empty()) {
                std::cout << "[Error] Cannot remove number" << std::endl;
                std::exit(1);
            } else {
                numberStack.pop();
            }
        } else {
            numberStack.push(number);
        }
    }

    while (!numberStack.empty()) {
        sum += numberStack.top();
        numberStack.pop();
    }
    
    // Output    
    std::cout << sum << std::endl;

    return 0;
}