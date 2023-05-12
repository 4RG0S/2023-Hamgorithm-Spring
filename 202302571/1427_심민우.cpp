#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool comp(char a, char b) {
    return a > b;
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string n;
    cin >> n;

    sort(n.begin(), n.end(), comp);

    cout << n;

    return 0;
}