#include <iostream>
#include <stack>
#include <string>

std::string brac(std::string str) {
    std::stack<char> bracket;
    for(int i = 0; i < str.size(); i++){
        if (str[i] == '(') {
            bracket.push(str[i]);
        }
        else {
            if(!bracket.empty())
                bracket.pop();
            else {
                return "NO";
            }
        }
    }
    if (!bracket.empty()) {
        return "NO";
    }
    else {
        return "YES";
    }
}

int main() {
    int N;
    std::cin >> N;
    for(int i = 0; i < N; i++) {
        std::string str;
        std::cin >> str;
        std::cout << brac(str) << std::endl;
    }
    return 0;
}
