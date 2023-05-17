#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n, m;
    cin >> n;
    vector<int> vec;
    set<int> s;
    for (int i=0; i<n;i++) {
        cin >> m;
        vec.push_back(m);
        s.insert(m);
        // cout << vec[i] << " ";
    }
    map<int, int> dict;
    int count = 0;
    for (int i : s) {
        dict[i] = count;
        count++;

    }

    for (int i : vec) {

        auto item = dict.find(i);
        cout << item->second<< ' ';
    }

    return 0;
}