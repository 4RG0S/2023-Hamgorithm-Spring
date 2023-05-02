#include <iostream>
#include <queue>

using namespace std;

queue<int> q;

int main() {
    int N, K, count=0, tmp;
    cin >> N >> K;
    for (int i=0; i < N; i++) {
        q.push(i+1);
    }
    cout << "<";
    while (!q.empty()) {
        tmp = q.front();
        q.pop();
        count++;
        if (count % K != 0) {
            q.push(tmp);
        } else {
            cout << tmp;
            if (!q.empty()) {
                cout << ", ";
            }
        }

    }
    cout << ">\n";

    return 0;
}

