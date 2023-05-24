#include <iostream>
#include <string>
#include <stack>
#include <vector>

bool isVPS(std::string str) {
    std::stack <char> stack;

    for(char c : str) {
        if(c == '(') {
            stack.push(c);
        } else if(c == ')') {
            if(stack.empty() || stack.top() != '(') {
                return false;
            }
            stack.pop();
        }
    }
    return stack.empty();
}

int main(void) {
    // Sync off
    std::ios_base::sync_with_stdio(false);

    // Declare variables
    ssize_t numberOfTestCases;
    std::vector <bool> resultVector;

    // Input number of testcases
    std::cin >> numberOfTestCases;

    // Loop
    for(ssize_t i = 0; i < numberOfTestCases; i++) {
        std::string str;
        std::cin >> str;

        if(isVPS(str)) {
            resultVector.push_back(true);
        } else {
            resultVector.push_back(false);
        }
    }

    for(bool result : resultVector) {
        if(result) {
            std::cout << "YES" << std::endl;
        } else {
            std::cout << "NO" << std::endl;
        }
    }

    return 0;
}
