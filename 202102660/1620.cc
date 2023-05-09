#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n >> m;
    string name;
    vector<string> vec(n+1);
    map<string, int> ma;
    for (int i=0; i < n; i++) {
        cin >> name;
        vec[i+1] = name;
        ma.insert(make_pair(name, i+1));
    }
    string instr;
    for (int i=0; i < m; i++) {
        cin >> instr;
        if (all_of(instr.begin(), instr.end(), ::isdigit)) {
            cout << vec[stoi(instr)] << '\n';
        } else {
            cout << ma[instr] << '\n';
        }
    }

    return 0;
}