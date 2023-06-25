#include <iostream>
#include <string>
#include <algorithm>

int main() {
    int N;
    std::string str;
    std::cin >> N;
    str = std::to_string(N);
    std::sort(str.begin(), str.end(), std::greater<char>());
    std::cout << str << std::endl;

    return 0;
}
