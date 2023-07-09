// 23.07.09
// BOJ 11286
// 우선순위 큐

#include <iostream>
#include <queue>

using namespace std;

int abs(int n) {
    if (n < 0)
        return -n;
    
    return n;
}

struct cmp { //비교연산자 구현
    bool operator()(int a, int b) {
        if (abs(a) == abs(b))
            return a > b;

        return abs(a) > abs(b);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    priority_queue<int, vector<int>, cmp> pq; //절대값 오름차
    while (n--) {
        int num;
        cin >> num;

        if (num == 0) {
            if (pq.empty())
                cout << "0 \n";
            else {
                cout << pq.top() << '\n';
                pq.pop();
            }
        }

        else
            pq.push(num);
    }

    return 0;
}