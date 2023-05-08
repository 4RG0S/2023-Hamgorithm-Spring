#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

vector<int> visiting(101, 0);

int search(vector<vector<int>>& vec, int from, int count, int n, deque<int> &q) {
    q.push_back(from);
    visiting[from] = 1;

    for (int i=1; i < vec[from].size(); i++) {
        int to = vec[from][i];
        if (visiting[to] == 0) {
            count = search(vec, to, count, n, q);
        }
    }
    q.pop_back();
    count++;
    return count;
}

int main() {
    // vector 저장. (from, to)
    // 주어진 노드 from 행 탐색 -> 큐에 지금꺼 넣고 -> 넣어진거 from 행 탐색 -> 반복..
    // 더이상 없으면 큐에서 뺌 -> 뺄 때마다 count
    int count=0;
    int n, m;
    deque<int> q;

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
    cout << count-1 << '\n';

    return 0;
}