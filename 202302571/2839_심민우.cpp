#include <iostream>

using namespace std;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    int sum = 0;

    bool check = false;
    while (n >= 0) {
        if (n % 5 == 0) {
            sum += n / 5;
            check = true;
            break;
        }
        n -= 3;
        sum++;
    }
    if (check)
        cout << sum;
    else
        cout << "-1";

    return 0;
}