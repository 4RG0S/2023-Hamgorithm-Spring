#include <iostream>
#include <vector>
#include <algorithm>
#include <list>

using namespace std;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;
    
    list<int> lt;
    vector<int> yose;

    for (int i = 1; i <= n; i++)
        lt.push_back(i);

    auto iter = lt.begin();
    while (!lt.empty()) {
        for (int i = 0; i < k - 1; i++) {
            iter++;
            if (iter == lt.end())
                iter = lt.begin();
        }
        yose.push_back(*iter);

        iter = lt.erase(iter);
        if (iter == lt.end())
            iter = lt.begin();
    }

    cout << "<";
    for (int i = 0; i < yose.size() - 1; i++)
        cout << yose[i] << ", ";
    cout << yose.back() << ">";
    

    return 0;
}