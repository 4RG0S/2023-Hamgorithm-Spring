#include <iostream>

int gcd(int a, int b) {
    int n = a % b;
    while(n != 0) {
        a = b;
        b = n;
        n = a % b;
    }
    return b;
}

int lcm(int a, int b) {
    return (a * b) / gcd(a,b);
}

int main() { 
    int a, b;
    std::cin >> a >> b;
    std::cout << gcd(a,b) << std::endl;
    std::cout << lcm(a,b) << std::endl;
}
