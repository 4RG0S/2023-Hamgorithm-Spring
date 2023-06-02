#include <iostream>
#include <string>
#include <stack>
#include <vector>

bool isBalance(std::string str) {
    std::stack<char> bracketManagementStack;

    for (char ch : str) {
        if (ch == '(' || ch == '[') {
            bracketManagementStack.push(ch);
        } else if (ch == ')' || ch == ']') {
            if (bracketManagementStack.empty()) {
                return false;
            }
            char top = bracketManagementStack.top();
            bracketManagementStack.pop();

            if ((ch == ')' && top != '(') || (ch == ']' && top != '[')) {
                return false;
            }
        }
    }

    return bracketManagementStack.empty();
}

int main(void) {
    // Sync off
    std::ios_base::sync_with_stdio(false);

    // Declare variables
    std::vector <bool> resultVector;

    // Input
    std::string input;
    while (std::getline(std::cin, input)) {
        if (input == ".") {
            break;
        }

        resultVector.push_back(isBalance(input));
    }

    // Output
    for(int i = 0; i < resultVector.size(); i++) {
        if(resultVector[i]) {
            std::cout << "yes\n";
        } else {
            std::cout << "no\n";
        }
    }

    return 0;
}
