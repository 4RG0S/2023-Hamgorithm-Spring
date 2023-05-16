#include <iostream>

using namespace std;

int main() {
    int n, m;

    cin >> n >> m;

    int mul = 1, div = 1;
    for (int i=0; i < m; i++) {
        mul *= (n-i);
        div *= (m-i);
    }
    // cout << mul << " " << div << '\n';
    cout <<(float)mul/div << '\n';
    return 0;
}