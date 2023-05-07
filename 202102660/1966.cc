#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

bool cmp(pair<int, int>& a, pair<int, int>& b) {
    return a.second < b.second;
}

deque<pair<int, int>> m1;

int main() {
    int c, n, m, temp;
    cin >> c;
    for (int i=0; i<c; i++) {
        cin >> n >> m;
        m1 = deque<pair<int, int>>();
        for (int j = 0; j<n; j++) {
            cin >> temp;
            m1.push_back(make_pair(j, temp));
        }
        int count = 0;
        while(!m1.empty()) {
            auto a = max_element(m1.begin(), m1.end(), cmp);
            auto f = m1.front();
            // cout << (*a).second << (*a).second;
            if (f.first == (*a).first) {
                count++;
                if (f.first == m) {
                    cout << count << '\n';
                    break;
                }
                m1.pop_front();

            } else {
                m1.pop_front();
                m1.push_back(f);
            }
        }
    }

    return 0;
}