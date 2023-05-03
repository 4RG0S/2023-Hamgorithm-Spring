#include <iostream>
#include <queue>
#include <string.h>

using namespace std;


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    deque<int> dq;

    int N, t;
    string temp;
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> temp;
        if (temp.compare("push_front") == 0) {
            cin >> t;
            dq.push_front(t);
        } else if (temp.compare("push_back") == 0) {
            cin >> t;
            dq.push_back(t);
        } else if (temp.compare("pop_front") == 0) {
            if (!dq.empty()) {
                t = dq.front();
                dq.pop_front();
                cout << t << '\n';
            } else {
                cout << "-1" << '\n';
            }
        } else if (temp.compare("pop_back") == 0) {
            if (!dq.empty()) {
                t = dq.back();
                dq.pop_back();
                cout << t << '\n';
            } else {
                cout << "-1" << '\n';
            }
        } else if (temp.compare("size") == 0) {
            cout << dq.size() << '\n';
        } else if (temp.compare("empty") == 0) {
            cout << dq.empty() << "\n";
        } else if (temp.compare("back") == 0) {
            if (!dq.empty()) {
                t = dq.back();
                cout << t << '\n';
            } else {
                cout << "-1" << '\n';
            }
        } else if (temp.compare("front") == 0) {
            if (!dq.empty()) {
                t = dq.front();
                cout << t << '\n';
            } else {
                cout << "-1" << '\n';
            }
        }
    }

    return 0;
}