#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int factorial(int n) {
    if (n == 0 || n == 1)
        return 1;

    int result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }

    return result;
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;
    cout << factorial(n) / (factorial(k) * factorial(n - k));

    return 0;
}