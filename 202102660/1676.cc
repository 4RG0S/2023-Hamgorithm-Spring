#include <iostream>
#include <string>

using namespace std;

int main() {
    int n, fact=1, count = 0;
    cin >> n;

    for (int i=5; i<(n+1); i*=5) {
        count += n/i;
    }
    cout << count << '\n';

    return 0;
}