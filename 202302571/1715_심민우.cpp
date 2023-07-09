// 23.07.06
// BOJ 1715
// 우선순위 큐

#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    priority_queue<int, vector<int>, greater<int>> pq; //우선순위 큐(오름차)
    int tmp = 0, sum = 0;

    for (int i =  0; i < n; i++) {
        cin >> tmp;
        pq.push(tmp);
    }

    //작은 거 2개 뽑아서 더하고 다시 push
    while (pq.size() > 1) {
        int p = pq.top();
        pq.pop();
        int q = pq.top();
        pq.pop();

        tmp = p + q;
        pq.push(tmp);
        sum += tmp;
    }

    cout << sum;

    return 0;
}