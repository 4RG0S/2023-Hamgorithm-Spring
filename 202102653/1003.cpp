#include <iostream>

// Global variable
long long fiboArr[50] = {0,1,};

long long fibo(int order) {
    if(order == 0 || order == 1)
        return fiboArr[order];
    else if(fiboArr[order] == 0)
        fiboArr[order] = fibo(order - 1) + fibo(order - 2);
    return fiboArr[order];
}

int main() {
    int numberOfTestCases;
    std::cin >> numberOfTestCases;
    int tempOrder;
    for(int i = 0; i < numberOfTestCases; i++) {
        std::cin >> tempOrder;
        if(tempOrder == 0) {
            std::cout << "1 0" << '\n';
        } else {
            std::cout << fibo(tempOrder - 1) << ' ' << fibo(tempOrder) << '\n';
        }
    }

    return 0;
}