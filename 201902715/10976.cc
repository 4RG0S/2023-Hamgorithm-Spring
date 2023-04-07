#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <queue>

using namespace std;

typedef long long ll;

int num_nodes, num_edges;
vector<int> graph[201];
int capacity[201][201], flow[201][201];
int previous[201];

int find_maximum_flow() {
    int result = 0;
    while (true) {
        queue<int> q;
        q.push(1);
        memset(previous, -1, sizeof(previous));
        previous[1] = 0;
        while (!q.empty()) {
            int current = q.front();
            q.pop();
            for (int next : graph[current]) {
                if (capacity[current][next] - flow[current][next] > 0 && previous[next] == -1) {
                    previous[next] = current;
                    q.push(next);
                    if (next == num_nodes) { break; }
                }
            }
        }
        if (previous[num_nodes] == -1) { break; }
        int current_flow = 999999999;
        for (int i = num_nodes; i != 1; i = previous[i]) {
            current_flow = min(current_flow, capacity[previous[i]][i] - flow[previous[i]][i]);
        }
        for (int i = num_nodes; i != 1; i = previous[i]) {
            capacity[previous[i]][i] -= current_flow;
            capacity[i][previous[i]] += current_flow;
        }
        result += current_flow;
    }
    return result;
}

int main() {
    int num_tests;
    cin >> num_tests;
    while (num_tests--) {
        cin >> num_nodes >> num_edges;
        for (int i = 1; i <= num_edges; i++) {
            int start, end;
            cin >> start >> end;
            if (start == 1 || end == num_nodes) { capacity[start][end] = 1; }
            else { capacity[start][end] = 999999999; }
            graph[start].push_back(end);
            graph[end].push_back(start);
        }
        cout << find_maximum_flow() << endl;
        for (int i = 1; i <= num_nodes; i++) {
            graph[i].clear();
        }
        memset(capacity, 0, sizeof(capacity));
        memset(flow, 0, sizeof(flow));
    }
    return 0;
}
