#include <iostream>
#include <vector>

int main() {
    int N;
    std::cin >> N;
    std::vector <long long> fib(N+1);

    fib[0] = 0;
    fib[1] = 1;
    fib[2] = 1;

    for(int i = 3; i < N+1; i++) {
        fib[i] = fib[i-1] + fib[i-2];
    }

    std::cout << fib[N];
}
