#include <iostream>
#include <queue>

using namespace std;

int main() {
    int N, tmp;
    queue<int> que;

    cin >> N;
    for(int i=1; i<N+1; i++) {
        que.push(i);
    }
    
    for(int i=1; ; i++) {
        if (que.empty()) {
            cout << tmp;
            break;
        }
        tmp = que.front();
        que.pop();
        if(i%2==0) {
            que.push(tmp);
        }
    }

    return 0;
}