#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

vector<int> visiting(101, 0);

int search(vector<vector<int>>& vec, int from, int count, int n, queue<int> &q) {
    q.push(from);
    visiting[from] = 1;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        count++;
        for (int i = 0; i < vec[cur].size(); i++) {
            int next = vec[cur][i];
            if(visiting[next] == 0) {
                visiting[next] = 1;
                q.push(next);
            }
        }

    }
    return count-1;
}

int main() {
    // vector 저장. (from, to)
    // 주어진 노드 from 행 탐색 -> 큐에 지금꺼 넣고 -> 넣어진거 from 행 탐색 -> 반복..
    // 더이상 없으면 큐에서 뺌 -> 뺄 때마다 count
    int count=0;
    int n, m;
    queue<int> q;

    cin >> n >> m;
    vector<vector<int>> nodes(n+1);

    int from, to;
    for (int i = 0; i < m; i++) {
        cin >> from >> to;
        nodes[from].push_back(to); 
        nodes[to].push_back(from);
    }
    from = 1;

    count = search(nodes, from, count, n, q);
    cout << count << '\n';

    return 0;
}