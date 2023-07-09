// 23.07.09
// BOJ 15903
// 우선순위 큐

#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long n, m;
    cin >> n >> m;

    priority_queue<long, vector<long>, greater<long>> card; //오름차순 우선순위 큐(int로 하면 오버플로우)
    for (long i = 0; i < n; i++) {
        long tmp;
        cin >> tmp;
        card.push(tmp);
    }

    while (m--) {
        //2개 뽑아서 더하고 2번 push
        long p = card.top(); card.pop(); 
        long q = card.top(); card.pop();

        card.push(p + q); card.push(p + q);
    }

    long sum = 0;
    while (n--) {
        sum += card.top();
        card.pop();
    }

    cout << sum;

    return 0;
}