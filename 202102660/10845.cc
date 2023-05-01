#include <iostream>
#include <queue>
using namespace std;
int main() {
    int N;
    string inst;
    queue<int> q;
    cin >> N;

    for (int i=0; i <N; i++) {
        cin >> inst;
        if (inst.compare("push") == 0) {
            int x;
            cin >> x;
            q.push(x);
        } else if (inst.compare("pop") == 0) {
            if (q.empty()) {
                cout << -1 << '\n';
            } else {
                cout << q.front() << '\n';
                q.pop();
            }
        } else if (inst.compare("size") == 0) {
            cout << q.size() << '\n';
        } else if (inst.compare("empty") == 0) {
            if (q.empty()) {
                cout << 1 << '\n';
            } else {
                cout << 0 << '\n';
            }
        } else if (inst.compare("front") == 0) {
            if (q.empty()) {
                cout << -1 << '\n';
            } else {
                cout << q.front() << '\n';
            }
        } else if (inst.compare("back") == 0) {
            if (q.empty()) {
                cout << -1 << '\n';
            } else {
                cout << q.back() << '\n';
            }
        } 
    }
}