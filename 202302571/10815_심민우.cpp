#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> card(n);
    for (int i = 0; i < n; i++)
        cin >> card[i];
    sort(card.begin(), card.end());

    int m;
    cin >> m;
    for (int i = 0; i < m; i++) {
        int inpt;
        cin >> inpt;

        if (binary_search(card.begin(), card.end(), inpt))
            cout << "1 ";
        else
            cout << "0 ";
    }

    return 0;
}